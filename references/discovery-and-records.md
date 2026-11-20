# Discovery and recordkeeping

## Search design

Combine region/cohort, art discipline, and an observable activity. Rotate between:

- Guangdong / Guangzhou / Shenzhen / city names and 26/27届, 高三, 统考, 联考.
- Art types: 美术, 音乐 plus instrument/曲目/视唱练耳, 播音/主持/传媒, 舞蹈 plus动作/剧目/训练, 书法 plus临摹/作品.
- Personal activities: 模考分数, 作品求评, 练习日常, 集训生活, 考试准备, 文化课返校/补习, parent questions about a child’s schedule or school.
- Comment paths: open posts that naturally attract peer discussion, then read comments and replies for first-person exam experiences, family statements, and direct course questions.

Search terms are discovery aids, not evidence. Open relevant results and verify recency, author identity, location context, and post body. Keep posts older than the requested window out of the active candidate list.

## Promotion filtering

Do not count an institution, teacher, agency, or promotion account as a customer merely because it uses a question-style title. Inspect its profile, repeated brand references, promotional structure, and comment pattern. Keep the post in the search archive as a reviewed/excluded sample. Check commenters independently; exclude generic praise, “加油,” and copied institution pitches unless the commenter supplies their own relevant situation.

## Suggested account schema

Each candidate record should include:

```json
{
  "platform": "小红书",
  "user_id": "stable public account ID",
  "name": "display name",
  "red_id": "",
  "profile_url": "https://www.xiaohongshu.com/user/profile/…",
  "account_type": "考生 | 家长 | 身份待核",
  "art_exam_types": ["美术"],
  "confidence": "高 | 中 | 低",
  "status": "候选，身份/年龄未经核实",
  "identity_basis": "本人/家长/评论者 evidence summary",
  "region_basis": "what supports or weakens Guangdong connection",
  "intent_basis": "what supports course interest, or state none",
  "reason": "short judgment with uncertainty",
  "last_seen": "ISO timestamp",
  "evidence": [
    {
      "source_type": "笔记作者 | 评论者",
      "note_title": "source title",
      "note_url": "source URL",
      "note_id": "source note ID",
      "observed_date": "YYYY-MM-DD",
      "excerpt": "short supporting excerpt"
    }
  ]
}
```

Store the full search responses and review log separately from this summarized candidate list. Keep excluded promotion examples and duplicate decisions so the same work is not repeated.

## Candidate vs. lead

Use “candidate account” when the account may be a Guangdong examinee or parent. Use “course-intent lead” only when a post/comment shows a current cultural-course need or a direct provider question. Preserve low-confidence cases for manual review; never inflate them into confirmed prospects.
