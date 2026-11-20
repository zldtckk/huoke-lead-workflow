# Huoke lead workflow skill

This package gives an AI agent a repeatable method for researching public art-exam prospect accounts, recording evidence, and syncing an authorized workbench snapshot.

## Contents

- `SKILL.md`: agent entry point and core workflow.
- `references/`: search/evidence rules and server-sync procedure.
- `scripts/sync_snapshot.py`: portable standard-library sync and count verification helper.
- `assets/.env.example`: safe configuration template with no credentials.

## Use with an AI agent

1. Unzip this folder.
2. If the AI supports skills, copy the folder into its skills directory and ask it to use `huoke-lead-workflow`.
3. Otherwise, attach `SKILL.md` and the relevant `references/*.md` files to the task prompt.
4. Give the AI access to the intended local project and an authenticated browser/data source. A skill package does not include platform cookies or accounts.
5. To sync, configure a destination-specific `.env` next to the snapshot, then run the helper. Do not send the `.env` file to the AI provider or include it in the ZIP.

Prompt to give another AI:

> Read and follow `huoke-lead-workflow/SKILL.md`. Use its references for search/review and sync. Work only in the project folder I provide, keep evidence and confidence labels, and never expose or copy credentials into output.

The sync helper uses Python 3's standard library; it requires no third-party package.

## Snapshot expectations

The workbench JSON should include a `records` array, a `prospect_accounts` array, and optionally `promotion_accounts`, `run_id`, and `updated_at`. The helper posts that entire snapshot; it does not collect data or call a paid search API.

## Privacy and security

This bundle intentionally excludes customer/account datasets, API keys, cookies, server passwords, SSH keys, and sync tokens. Store public-source evidence minimally, keep confidence and uncertainty visible, and never contact accounts automatically.
