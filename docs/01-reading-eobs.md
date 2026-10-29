# Step 1: Reading Your Explanation of Benefits (EOB)

Before you can appeal a denial, you need to understand *what* was denied and
*why*. That information lives on your EOB. This page walks you through reading
one — even if it looks like a wall of text and numbers.

---

## What an EOB looks like

EOBs vary by insurer, but they all contain roughly the same sections. Here is
the typical layout:

```
┌─────────────────────────────────────────────────────────┐
│  Patient Information           Claim Information         │
│  Name, DOB, Member ID          Claim Number, Date       │
├─────────────────────────────────────────────────────────┤
│  Summary                                              │
│  - Total billed amount                                  │
│  - Insurer-paid amount                                 │
│  - Patient responsibility (copay, deductible, coinsurance)│
│  - Denial reason (if applicable)                        │
├─────────────────────────────────────────────────────────┤
│  Service Details (one row per service)                │
│  Date  | CPT/HCPCS Code | Description | Billed | Paid | Patient│
├─────────────────────────────────────────────────────────┤
│  Remarks / Explanation                                  │
│  Free-text explanation of any adjustments or denials    │
├─────────────────────────────────────────────────────────┤
│  Next Steps                                             │
│  - Appeal rights, deadline, contact info                 │
└─────────────────────────────────────────────────────────┘
```

You may receive the EOB by mail, in an insurer portal, or as an email
attachment. Regardless of format, the same information is there.

---

## Section by section

### 1. Patient and Claim Information

| Field | What to look for |
|-------|-----------------|
| **Patient name and date of birth** | Confirm this matches you. If it does not, the claim was sent to the wrong insurer. |
| **Subscriber/member ID** | Your insurance card number. Write it down. |
| **Claim number** | A unique identifier (often starts with `CLM` or `H`). You will need this on every appeal letter. |
| **Date of service** | The date or date range the service was provided. This must match your records. |
| **EOB date / Received date** | The date the insurer processed the claim. Your deadline clock usually starts here. |

### 2. Summary (also called "Payment Summary" or "Explanation")

This is the top section that shows the big numbers:

- **Total billed (or "Billed charges")** — What the provider submitted.
- **Allowed amount** — What the insurer says is reasonable for this service.
- **Insurer-paid** — What the insurer actually paid.
- **Patient responsibility** — What you owe (copay, deductible, coinsurance, or the full amount if denied).

> **If "Insurer-paid" is $0.00 and "Patient responsibility" matches the full
> billed amount, the claim was denied.** This is the most common denial scenario.

### 3. Denial Reason Codes

This is the most important section. Insurers use standardized codes to explain
why they denied or reduced payment. Here are the most common categories:

#### **CO codes (Claims Adjustment Reason Codes / CARCs)**

Issued by the provider's billing office and the insurer.

| Code | Meaning | What it means for you |
|------|---------|----------------------|
| CO-29 | "Charges are above the plan's allowance" | The provider billed more than the negotiated rate. You may still be responsible for your coinsurance on the *allowed* amount. |
| CO-30 | "A third party is responsible" | The insurer thinks someone else should pay. You may need to involve the other party. |
| CO-45 | "Requested information not provided" | The insurer needs more documentation. Gather the missing records and resubmit. |
| CO-48 | "Re-submission of a claim with different revenue centers" | Administrative error — ask the provider to correct and resubmit. |
| CO-95 | "The benefit for this service is included in another benefit" | The service is bundled into another one. |

#### **PR codes (Patient Responsibility codes / Remittance Advice Remark Codes)**

These tell you what, if anything, you owe.

| Code | Meaning |
|------|---------|
| PR-1 | Deductible not met |
| PR-2 | Coinsurance applicable |
| PR-3 | Copayment applicable |
| PR-62 | Non-covered service |
| PR-150 | Provider not in network |
| PR-152 | Amount conterminous with another payer |
| PR-165 | Not covered unless certified in advance |

#### **RP codes (Remittance Advice Remark Codes)**

These give more detail about *why* a service was adjusted.

| Code | Meaning |
|------|---------|
| RP-1006 | "Service not covered by benefit" |
| RP-160 | "Charges exceed the fee schedule" |
| RP-22 | "Documentation not sufficient to determine severity" |
| RP-455 | "Prior authorization required" |

> **Pro tip:** Write down the exact code and its description. You will reference
> it in your appeal letter. Insurers often have a code lookup tool on their
> website.

### 4. Service Details Table

Each row in this table represents one service that was billed. For each service,
check that:

- The **date of service** matches what you (or your provider) recorded.
- The **CPT or HCPCS code** matches the service you received.
- The **description** makes sense for the service.
- The **billed** and **paid** amounts look correct.

If any of these are wrong, note it down. Billing errors are grounds for appeal.

---

## Common EOB red flags

| Red flag | What it might mean |
|----------|--------------------|
| Service dates you don't recognize | The provider may have billed for services you didn't receive, or there is an identity mix-up. |
| A code you don't recognize | Look it up. Many codes have specific meanings that affect coverage. |
| "Patient responsibility" equals the full billed amount | The service was likely denied in full. |
| Multiple EOBs for the same claim number | The claim may have been re-processed. Check each EOB. |
| No denial reason listed | Request a detailed explanation in writing. |

---

## How to keep a paper trail

For every EOB you receive, record:

| Field | Value (example) |
|-------|-----------------|
| EOB received date | 2026-10-20 |
| Date of service | 2026-10-05 |
| Claim number | CLM123456789 |
| Denial code | CO-45 |
| Patient responsibility | $247.50 |
| Appeal deadline | 2027-04-16 (180 days from EOB) |
| Notes | Provider says prior auth was sent but not received |

A simple spreadsheet (Google Sheets, Excel, or even a text file) is all you need.
We cover spreadsheet templates in [Step 4](04-tracking-deadlines.md).

---

## Quick checklist: Before you move on

- [ ] You have recorded the EOB received date.
- [ ] You have recorded the claim number.
- [ ] You have identified the denial reason code(s).
- [ ] You have confirmed the date of service and total patient responsibility.
- [ ] You have noted the appeal deadline (we will confirm this in Step 4).

---

## Try it with AI

Once you have your EOB in front of you, you can paste the text into an AI tool
with the following kind of prompt (see `docs/prompts/eob-reading-prompt.md` for
a ready-to-use template):

> "I received this EOB text from my insurance company. Please identify:
> (1) the claim number, (2) the date of service, (3) the denial reason code and
> its plain-English meaning, and (4) the patient responsibility amount. Return
> the results in a table."

---

Copyright (c) 2026 Asdale Dynamics, LLC.
