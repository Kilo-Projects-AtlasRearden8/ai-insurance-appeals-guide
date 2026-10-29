# AI Prompt: Reading an Explanation of Benefits (EOB)

Use this prompt when you want an AI tool to help you understand your EOB.
Paste only sanitized text — mask your member ID, claim number (middle digits),
address, and phone number before sharing with any AI.

## When to use this

After you have received an EOB with a denial or adjustment and you want to:
- Identify the claim number and dates.
- Understand what the denial code means in plain English.
- Find the patient responsibility amount.
- Confirm the service details.

## Prompt (copy and customize)

```
I received the following Explanation of Benefits (EOB) text from my insurance
company. Personal details have been masked. Please help me identify:

1. The claim number.
2. The date of service (start and end if applicable).
3. The denial reason code(s) and what each means in plain English.
4. The total billed amount, insurer-paid amount, and patient responsibility.
5. Whether this appears to be a full denial, partial denial, or no denial.
6. Any appeal deadline mentioned in the text.

EOB text:
---
[Paste your sanitized EOB text here]
---

Please return the results as a table with columns: Item | Detail | Notes.
If you cannot determine something from the text, say "Not shown" instead of
guessing. Do not invent dates, codes, or amounts.
```

## Tips for best results

- Paste only the relevant pages of the EOB. You do not need to include the
  cover page or general marketing text.
- Mask your member ID: `XXXX[[MASKED]]1234`.
- Mask your claim number: `CLM[[MASKED]]9876`.
- Replace your name with `[Patient]` and your address with `[Redacted]`.
- Keep all dollar amounts and codes visible — those are not personal
  identifiers.

## Verify before trusting

AI may misread denial codes. After using this prompt, check each code against
your insurer's official code list (usually on their website or in your plan
document).

---

Copyright (c) 2026 Asdale Dynamics, LLC.
