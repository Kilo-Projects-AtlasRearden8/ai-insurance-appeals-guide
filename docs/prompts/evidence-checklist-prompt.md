# AI Prompt: Evidence Checklist Generator

Use this prompt to generate a simple evidence-gathering checklist tailored to
your denial reason and the service you are appealing.

## When to use this

After you have read your EOB and identified the denial code, and you want a
structured list of documents to collect.

## Prompt (copy and customize)

```
I am appealing an insurance denial and need an evidence checklist. Here are
the facts:

- Service: [brief description of the medical service]
- Date of service: [date]
- Denial code: [CODE] — [plain English meaning]
- Denied amount: $[amount]
- Evidence I already have: [list what you have]
- Evidence I still need: [list what you think you need]

Please generate a simple checklist table with these columns:
  1. Document (name)
  2. What it proves
  3. Where to get it
  4. Have it? (Yes/No/Partial)
  5. Notes

Keep the language simple and beginner-friendly. Do not include legal advice
or guarantee that collecting these documents will result in approval. Use
placeholders like [Provider Name] where personal details would go.
```

## Example output format

| Document | What it proves | Where to get it | Have it? | Notes |
|----------|----------------|-----------------|----------|-------|
| EOB (Claim CLM...) | Shows denial code and amount | Your insurer's portal | Yes | |
| Medical records | Supports medical necessity | Provider's records dept | Partial | Requested Oct 22 |
| Physician statement | Explains why service was necessary | Your doctor's office | No | Ask Dr. Smith |

---

Copyright (c) 2026 Asdale Dynamics, LLC.
