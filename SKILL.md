---
name: huoke-lead-workflow
description: Find and assess public Xiaohongshu prospect accounts for Guangdong art-exam and cultural-course services, preserve evidence locally, and sync a workbench snapshot to an authorized endpoint. Use when asked to discover, review, deduplicate, archive, or sync these prospect leads.
metadata:
  short-description: Art-exam prospect research and workbench sync
---

# Huoke lead workflow

Use this skill for public social-media research and authorized workbench synchronization. The target market, province, art disciplines, freshness window, and destination can be changed per task.

## Workflow

1. Identify the requested customer, region, disciplines, and recency window from the conversation. Default to Guangdong and the most recent 183 days only when those defaults fit the request.
2. Check the existing local account library and known promotion-account library before searching. Deduplicate by platform plus stable account ID; also compare profile URL, display name, and evidence note ID when IDs are transformed by a provider.
3. Search public notes through an authenticated browser session or an explicitly configured data provider. Record the source, query, date, provider/API cost, and errors. Never put API keys, cookies, passwords, or sync tokens in notes or output.
4. Read the full relevant note and useful comments. Separate the poster from commenters. A promotional post can contain genuine prospective commenters; assess each person on their own evidence.
5. Classify promotion, student/parent identity, art discipline, Guangdong connection, and service intent separately. Keep uncertain records as low-confidence candidates; do not label them confirmed customers.
6. Save every search result and review decision locally before syncing. Keep each batch, the aggregate account library, and the current workbench snapshot distinct.
7. Sync only to a user-authorized endpoint with credentials already configured. Use `scripts/sync_snapshot.py` to push and verify the account count. Do not send comments, follow accounts, or contact prospects unless separately requested and authorized.

## Evidence standards

- Strong identity evidence: first-person exam preparation, a specific art discipline and cohort, family statements about their own child, or a direct course-selection question.
- Guangdong evidence is separate: explicit Guangdong exam/location context is stronger than an IP label or hashtag alone. A non-Guangdong IP does not by itself exclude a Guangdong candidate.
- Promotion signals include repeated brand mentions, institution-style visuals, templated conversion copy, testimonials centered on one provider, and many institution accounts replying. Writing style alone is not enough to label a post as promotion.
- Intent signals include asking for a course/provider, comparing class formats or costs, requesting local recommendations, or describing a current cultural-course problem. Being an art examinee alone is not proof of purchase intent.
- Use high/medium/low confidence and preserve the exact short excerpt and source URL that support the judgment. Do not infer age, collect private contact details, or enrich identities from unrelated sources.

## References

- Read [references/discovery-and-records.md](references/discovery-and-records.md) for query patterns, promotion filtering, deduplication, and the account schema.
- Read [references/sync-and-credentials.md](references/sync-and-credentials.md) before connecting to a server or pushing data.
- The portable sync helper is [scripts/sync_snapshot.py](scripts/sync_snapshot.py). Its configuration example is [assets/.env.example](assets/.env.example).
