# Sync and credentials

## Configuration

Copy `assets/.env.example` to a local `.env` beside the snapshot and fill the destination’s authorized values. Keep `.env` out of archives and version control. Environment variables override the `.env` file:

- `WORKBENCH_SYNC_URL`: site root, for example `https://huoke.msrtai.site`.
- `WORKBENCH_SYNC_TOKEN`: server-side bearer token configured for `POST /api/sync`.

The sync token is independent of SSH credentials and web Basic Auth. A successful website page load or a successful read-only `GET /api/prospect-accounts` does not prove write access.

## Current Tencent setup

For the Huoke workbench, the Tencent host and current account are in the user’s desktop `服务器.txt`; read it locally without printing credentials. SSH port 22 was reachable and password authentication for `ubuntu` succeeded. The available local public keys were rejected, so a public-key-only attempt can fail even while password login works. The sync token is stored server-side in `/etc/xhs-workbench.env`; retrieve only `WORKBENCH_SYNC_TOKEN` over an authenticated SSH session, without echoing the file into logs.

The Huoke project keeps the local token in `deploy/tencent/.env`, which is gitignored. For another server, use its own authorized host, account, token path, and destination; do not reuse this project’s credentials.

## Push and verify

The snapshot must be a JSON object with at least a `records` array and a `prospect_accounts` array. Run:

```powershell
python scripts/sync_snapshot.py --snapshot path\to\workbench_current.json --env-file path\to\.env
```

The helper posts the snapshot to `/api/sync`, checks the server’s confirmed candidate count, then reads `/api/prospect-accounts` and confirms the same count. It prints counts and run ID only, never the bearer token or response body. HTTP 401 indicates missing/incorrect sync credentials; connection timeouts indicate network/service reachability; count mismatches indicate a server-side persistence or payload problem.

For the source Huoke project, `python sync_workbench.py --sync-current` uses the local `.env` and performs the same verification.
