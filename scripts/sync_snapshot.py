#!/usr/bin/env python3
"""Push a workbench JSON snapshot to an authorized endpoint and verify counts."""

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

MAX_PAYLOAD_BYTES = 20 * 1024 * 1024


def read_env_file(path):
    values = {}
    if not path.exists():
        return values
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def request_json(request, timeout):
    with urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def sync_snapshot(snapshot_path, env_path):
    settings = read_env_file(env_path)
    base_url = os.environ.get("WORKBENCH_SYNC_URL", "").strip() or settings.get("WORKBENCH_SYNC_URL", "").strip()
    token = os.environ.get("WORKBENCH_SYNC_TOKEN", "").strip() or settings.get("WORKBENCH_SYNC_TOKEN", "").strip()
    if not base_url or not token:
        raise ValueError("WORKBENCH_SYNC_URL and WORKBENCH_SYNC_TOKEN are required.")

    raw = snapshot_path.read_bytes()
    if len(raw) > MAX_PAYLOAD_BYTES:
        raise ValueError("Snapshot exceeds the server's 20 MiB request limit.")
    snapshot = json.loads(raw.decode("utf-8"))
    if not isinstance(snapshot, dict) or not isinstance(snapshot.get("records"), list):
        raise ValueError("Snapshot must be an object containing a records array.")
    accounts = snapshot.get("prospect_accounts")
    if not isinstance(accounts, list):
        raise ValueError("Snapshot must contain a prospect_accounts array.")

    body = json.dumps({"workbench": snapshot}, ensure_ascii=False).encode("utf-8")
    post = Request(
        base_url.rstrip("/") + "/api/sync",
        data=body,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        confirmation = request_json(post, timeout=30)
    except HTTPError as exc:
        raise RuntimeError(f"Sync endpoint returned HTTP {exc.code}.") from None
    except (URLError, TimeoutError) as exc:
        raise RuntimeError(f"Sync request failed: {type(exc).__name__}.") from None
    if not confirmation.get("ok"):
        raise RuntimeError("Server did not confirm the sync.")
    expected = len(accounts)
    if confirmation.get("prospect_account_count") != expected:
        raise RuntimeError("Server confirmation count does not match the snapshot.")

    get = Request(base_url.rstrip("/") + "/api/prospect-accounts")
    try:
        live = request_json(get, timeout=20)
    except (HTTPError, URLError, TimeoutError) as exc:
        raise RuntimeError(f"Sync was accepted, but live verification failed: {type(exc).__name__}.") from None
    live_accounts = live.get("accounts", []) if isinstance(live, dict) else live
    if not isinstance(live_accounts, list) or len(live_accounts) != expected:
        raise RuntimeError("Live account count does not match the snapshot.")
    return {
        "ok": True,
        "run_id": confirmation.get("run_id"),
        "note_count": confirmation.get("note_count"),
        "prospect_account_count": len(live_accounts),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", required=True, type=Path, help="workbench JSON file")
    parser.add_argument("--env-file", type=Path, default=Path(".env"), help="gitignored environment file")
    args = parser.parse_args()
    try:
        result = sync_snapshot(args.snapshot, args.env_file)
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"Sync failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
