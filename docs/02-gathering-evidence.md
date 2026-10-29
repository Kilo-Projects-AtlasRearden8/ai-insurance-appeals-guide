# Step 2: Gathering Evidence

A strong appeal needs evidence. The insurance company needs to understand *why*
they should cover a service they initially denied. This page explains what
documents to collect and how to organize them.

---

## What counts as "evidence"?

Evidence is any document that supports your case. The most powerful evidence
directly contradicts the insurer's stated reason for denial. Here are the main
types:

| Document | What it proves | Where to get it |
|----------|----------------|-----------------|
| **Medical records** | The service was medically necessary | Your provider's office |
| **Physician statement** | Your doctor explains why the treatment was necessary | Your doctor writes it |
| **Prior authorization** | You (or your provider) got approval before the service | Provider's office or insurer portal |
| **Claim resubmission records** | Previous attempts to get paid | Your provider's billing office |
| **Insurance plan document** | The service *is* covered under your plan | Your insurer's website or member services |
| **Timely filing proof** | The claim was submitted on time | Receipts, emails, call logs |
| **Payment history** | You have paid your share on time | Bank statements, receipts |

---

## Step 2a: Request your medical records

Medical records are the backbone of most successful appeals. Here is how to get
them:

### 1. Identify the records custodian

Every healthcare provider has a **records department** (sometimes called Health
Information Management or HIM). Call or visit the provider's main phone number
and ask for the records department.

### 2. Submit a written request

Verbal requests are easy to ignore. Write a short letter or email:

> "Please provide complete medical records for patient [Your Name], DOB
> [date], for the period [date range]. This includes all notes, lab results,
> imaging reports, and correspondence related to [service description] performed
> on [date of service]. I am requesting these records to file an insurance
> appeal. Please send copies to: [your mailing address or email]."

> **By law**, in the U.S., providers must respond to medical record requests
> within 30 days (some states require faster turnaround). If they miss the
> deadline, note it in your appeal.

### 3. Track your request

Record:
- The date you submitted the request.
- The name of the person you spoke with (if called).
- A confirmation number or email.
- The expected delivery date.

---

## Step 2b: Get a physician statement

If the denial was based on "not medically necessary," a letter from your doctor
is critical. The physician statement should explain:

1. **Your diagnosis** (the medical condition).
2. **Why the specific service was necessary** (not optional or experimental).
3. **What would happen without it** (risks of not treating).
4. **Alternative treatments tried** (if any).

A good physician statement is usually one page. If your doctor's office has a
template, use it. If not, you can use AI to help draft the structure — but your
doctor must write and sign it themselves. Never fabricate a doctor's signature.

---

## Step 2c: Check for prior authorization

Many denials happen because prior authorization was never obtained. If your
provider says they sent it, ask for:

- A copy of the prior authorization request (the form).
- The submission date.
- The reference number.
- The response (approved, denied, or "missing information").

If the insurer says they never received it, you have evidence of an
administrative error — and you can appeal on that basis.

---

## Step 2d: Review your plan document

Your plan documents (Summary of Benefits and Coverage, Evidence of Coverage)
describe exactly what is and is not covered. When an insurer denies a claim,
check the plan document to see if their interpretation matches.

### How to find your plan document

1. Log in to your insurer's member portal.
2. Search for "Evidence of Coverage," "Plan Benefits," or "Member Handbook."
3. Download the PDF and search (Ctrl+F) for the service code or description.

If the plan document says the service *is* covered, but the insurer denied it,
that is a strong basis for appeal.

---

## Step 2e: Organize your evidence

### Naming convention

Use a clear, consistent naming system:

```
[LastName]_[ClaimNumber]_[DocumentType]_[Date].pdf
```

Examples:
```
Asdale_CLM123456789_EOB_2026-10-20.pdf
Asdale_CLM123456789_MedicalRecords_2026-10-22.pdf
Asdale_CLM123456789_PhysicianStatement_2026-10-25.pdf
Asdale_CLM123456789_PlanDocument_2026-10-20.pdf
```

### Folder structure

```
appeal-files/
  01-claims/
    CLM123456789/
      eob.pdf
      denial-letter.pdf
      medical-records.pdf
      physician-statement.pdf
      plan-document.pdf
  02-evidence-tracker.xlsx
  03-correspondence/
    2026-10-25_appeal-letter-draft.docx
    2026-10-27_insurer-response.pdf
```

### Checklist of evidence to collect

- [ ] Copy of the EOB (with denial codes visible).
- [ ] Copy of the denial letter (if separate from EOB).
- [ ] Medical records for the relevant date(s).
- [ ] Physician statement (if denial is based on medical necessity).
- [ ] Copy of the prior authorization (if applicable).
- [ ] Copy of your plan's coverage document.
- [ ] Proof of timely filing (if the insurer claims the claim is late).
- [ ] Receipts for any payments you made (deductible, copay).

---

## What NOT to include

- **Your Social Security Number** — redact it from any document you submit.
- **Other family members' medical records** — only include records relevant to
  the denied service.
- **Unrelated services** — keep the appeal focused.

---

## Quick checklist: Before you move on

- [ ] You have requested medical records from your provider.
- [ ] You have a physician statement (if needed for medical necessity).
- [ ] You have checked for prior authorization documentation.
- [ ] You have located your plan's coverage document.
- [ ] All documents are organized in a dated, labeled folder.

---

## Try it with AI

You can use AI to help you create an evidence checklist and organize your
documents. See `docs/prompts/evidence-checklist-prompt.md` for a ready-to-use
template:

> "I am appealing an insurance denial for [service] on [date]. The denial code
> is [code]. Please generate a checklist of evidence I should gather, with
> columns for: document name, what it proves, where to get it, whether I have
> it, and notes. Keep it simple for a beginner."

---

Copyright (c) 2026 Asdale Dynamics, LLC.
