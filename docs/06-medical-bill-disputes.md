# Step 6: Medical Bill Dispute Letters

Sometimes the problem isn't a denial — it's a bill that just looks wrong. You
might be charged the full price instead of your copay, billed for a service you
never received, or charged twice for the same thing. This page shows you how to
dispute a medical bill, step by step.

Education only — this is not billing advice. Always verify charges with your
provider's billing office or insurer.

---

## Bill vs. EOB: your side-by-side check

Before you dispute anything, compare your **medical bill** (from the provider)
with your **Explanation of Benefits** (from the insurer). They should tell the
same story.

| Item | On your bill | On your EOB | Do they match? |
|------|--------------|-------------|----------------|
| Date of service | | | |
| Provider name | | | |
| Service / CPT code | | | |
| Total billed | | | |
| Insurer paid | — | | |
| What you owe | | | |

If the bill shows you owe more than the EOB's "patient responsibility," that's
a red flag worth disputing.

---

## Common billing errors worth disputing

| Error | What it looks like | What to do |
|-------|-------------------|------------|
| Billed full price instead of negotiated rate | Your bill says $450, but EOB allowed amount is $200 | Dispute — ask for the negotiated rate |
| Duplicate charge | Same service, same date, two line items | Dispute — request removal of duplicate |
| Service not received | You don't recognize the date or service | Dispute — request medical records to verify |
| Wrong patient | Bill has someone else's name or DOB | Call billing office immediately |
| Balance billing | In-network provider billed above allowed amount | Dispute — may violate your contract |
| Unmet deductible applied twice | Deductible charged on multiple services for one visit | Dispute — deductible applies once per period |

---

## How to write a dispute letter

A good dispute letter is short, factual, and includes your evidence. Here's the
structure:

```
1. Your contact information
2. Date
3. Provider billing department name and address
4. Subject line: "RE: Bill Dispute — Account #[number] — Date of Service [date]"
5. Account number, date of service, billed amount
6. Statement of dispute (one sentence: "I dispute this bill because...")
7. Summary of the issue (factual, 2-4 sentences)
8. Comparison table: billed amount vs. EOB-paid vs. what you owe
9. Evidence attached
10. Specific request (e.g., "correct the bill and issue a revised statement")
11. Signature and printed name
```

### Sample dispute letter template

```text
[Your Name]
[Your Street Address]
[City, State ZIP]
[Phone] | [Email]

[Date]

[Provider Name] — Billing Department
[Billing Address]
[City, State ZIP]

RE: Bill Dispute — Account #[NUMBER] — Date of Service [Month DD, YYYY]

Account Number: [XXXXXXXXX]
Date of Service: [Month DD, YYYY]
Billed Amount: $[amount]

I am writing to dispute the bill referenced above. I believe the amount
charged is incorrect and request a corrected statement.

On [date of service], I received [service] from [provider]. My bill shows a
charge of $[amount]. However, my Explanation of Benefits shows my insurer
allowed $[amount] and paid $[amount], leaving a patient responsibility of
$[amount] — not $[amount].

| Item | My bill | EOB (insurer) | Difference |
|------|---------|---------------|------------|
| Billed amount | $[amount] | $[amount] | $[amount] |
| Allowed amount | — | $[amount] | — |
| Insurer paid | — | $[amount] | — |
| Patient responsibility | $[amount] | $[amount] | $[amount] |

Enclosed:
  - Copy of my bill (dated [date])
  - Copy of my Explanation of Benefits (dated [date])

I request that you correct this bill and issue a revised statement
reflecting the accurate patient responsibility. Please send written
confirmation to the address above.

Thank you for your time and consideration.

[Signature]
[Printed Name]
```

---

## How to use AI to draft your dispute letter

AI is good at turning your bullet points into a polite, professional letter.
Use the prompt in `docs/prompts/dispute-letter-prompt.md`. Here's the
simplified version:

> "I need to write a medical bill dispute letter. Here are the facts: [list
> facts including account number, date of service, billed amount, EOB amount,
> and why you think it's wrong]. Please write a professional dispute letter
> with a subject line, a factual summary, a comparison table, and a specific
> request. Keep the tone respectful. Replace all personal details with
> placeholders."

### Review AI output before sending

- [ ] Replace every `[placeholder]` with real information.
- [ ] The account number matches your bill exactly.
- [ ] The billed amount and EOB amounts match your actual documents.
- [ ] The evidence list only includes documents you actually have.
- [ ] No emotional language or accusations — stick to the facts.
- [ ] The amount you request is specific and math-checks out.

---

## Send it & track the response

- **Send by certified mail** (return receipt requested) if mailing, so you have
  proof of delivery. Or use the provider's secure patient portal if they offer
  one.
- **Note the date you sent it** and any confirmation number.
- **Set a calendar reminder** to follow up in 2–3 weeks if you haven't heard
  back.
- **Save a dated copy** of the letter and everything you receive in response.

---

## Quick checklist: Before you move on

- [ ] You compared your bill and EOB side by side.
- [ ] You identified the specific error you're disputing.
- [ ] Your letter includes: your info, date, billing address, subject line,
  account number, date of service, and billed amount.
- [ ] You clearly state what you dispute and why.
- [ ] You included a comparison table with real numbers.
- [ ] You listed every enclosed document.
- [ ] You reviewed and edited any AI-generated text (no placeholders left).
- [ ] You saved a dated copy and noted the send date.

---

## Try it with AI

See `docs/prompts/dispute-letter-prompt.md` for a ready-to-use template:

> "I need to write a medical bill dispute letter. Here are the facts (all
> personal details replaced with placeholders): ..."

---

Copyright (c) 2026 Asdale Dynamics, LLC.
