# Sync and credentials

## Configuration

Copy `assets/.env.example` to a local `.env` beside the snapshot and fill the destination’s authorized values. Keep `.env` out of archives and version control. Environment variables override the `.env` file:

- `WORKBENCH_SYNC_URL`: site root, for example `https://huoke.msrtai.site`.
- `WORKBENCH_SYNC_TOKEN`: server-side bearer token configured for `POST /api/sync`.

The sync token is independent of SSH credentials and web Basic Auth. A successful website page load or a successful read-only `GET /api/prospect-accounts` does not prove write access.

## Server connection

Use the owner-provided credential source for the target server. Keep the host, username, password, private key, and token out of the skill, Git history, command output, and AI prompt. Verify the host key. A reachable SSH port only proves network reachability; rejected public-key authentication does not prove that password authentication or the server itself is unavailable. Use the authorized method and account instead of guessing credentials.

After SSH authentication, retrieve only the `WORKBENCH_SYNC_TOKEN` value from the server’s configured environment file. Do not echo the full environment file to terminal output or logs. Store the value in the local gitignored `.env`. For another server, use its own authorized host, account, token path, and destination; do not reuse this project’s credentials.

## Push and verify

The snapshot must be a JSON object with at least a `records` array and a `prospect_accounts` array. Run:

```powershell
python scripts/sync_snapshot.py --snapshot path\to\workbench_current.json --env-file path\to\.env
```

The helper posts the snapshot to `/api/sync`, checks the server’s confirmed candidate count, then reads `/api/prospect-accounts` and confirms the same count. It prints counts and run ID only, never the bearer token or response body. HTTP 401 indicates missing/incorrect sync credentials; connection timeouts indicate network/service reachability; count mismatches indicate a server-side persistence or payload problem.

For the source Huoke project, `python sync_workbench.py --sync-current` uses the local `.env` and performs the same verification.
