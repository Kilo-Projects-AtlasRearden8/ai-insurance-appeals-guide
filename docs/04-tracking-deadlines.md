# Step 4: Tracking Deadlines

Missing a filing deadline is the most common reason appeals fail — not because
the argument was weak, but because the insurer is no longer required to consider
it. This page shows you how to track deadlines so you never miss one.

---

## Why deadlines matter

Every denial triggers one or more deadlines. Miss one, and your right to appeal
that specific denial expires. The clock typically starts on the **EOB date** or
the **denial letter date** — not the date you discover the denial.

---

## Common deadline types

| Deadline type | Typical length | When it starts |
|---------------|----------------|----------------|
| **Internal appeal** | 180 days | EOB date or denial letter date |
| **External review (request)** | Usually 45–60 days from internal denial | Date of internal appeal decision |
| **External review (hearing)** | Varies by state | Date of external review request |
| **Renewed internal appeal** | 60–90 days | If you get new evidence after the first appeal |
| **Health plan grievance** | 180 days (some plans 90) | EOB date |

> **These timelines vary by state and plan.** Check your plan document and the
> denial letter for the exact deadline. When in doubt, assume the shorter period
> applies.

---

## How to find your specific deadline

### 1. Check the denial letter (not just the EOB)

Many plan members stop at the EOB. The denial letter — sometimes a separate
document — usually states the deadline in plain text:

> "You have 180 days from the date of this letter to appeal this decision."

### 2. Check your plan's Summary of Benefits

Look for a section called "Appeals" or "Grievances and Appeals." It will list
the standard timeframes.

### 3. Check your state's insurance regulations

Most states require a minimum of 180 days for internal appeals. You can search
"[Your state] insurance appeal deadline."

### 4. Call member services

Ask specifically: "What is the deadline to appeal claim [number]?" Write down
the name of the representative and the date of the call.

> **Pro tip:** If a representative gives you a different deadline than what is
> in writing, go with the *shorter* one. When you have two conflicting
> deadlines, use the earlier date.

---

## How to track deadlines

You do not need expensive software. Here are three options, from simplest to
most powerful.

### Option A: A simple table (Google Sheets or Excel)

Create a spreadsheet with these columns:

| Claim | Denial Date | Deadline | Days Remaining | Status | Notes |
|-------|-------------|----------|----------------|--------|-------|
| CLM123... | 2026-10-20 | 2027-04-16 | 69 | Draft letter | |

Use these formulas:
- **Days Remaining:** `=Deadline - TODAY()` (format as a number)
- **Highlight past due:** Conditional formatting → cells less than today → red fill.
- **Highlight approaching:** Conditional formatting → cells within 14 days → yellow fill.

### Option B: A wall calendar

Mark every denial date with a red circle. Then count 180 days forward and mark
the deadline with a bold X. Add a reminder 14 days before the deadline.

### Option C: Digital tools

- **Google Calendar** — Create an event on the deadline date, then set a
  reminder 14 days prior.
- **Todoist / Things / Microsoft To Do** — Create a task with a due date.
- **Airtable** — If you want linked records between claims, evidence, and
  correspondence.

---

## What to do when a deadline is near

| Days remaining | Action |
|----------------|--------|
| 30+ | No rush, but review the evidence. |
| 30–14 | Draft the appeal letter and gather documents. |
| 14–7 | Schedule a final review. Send early if possible. |
| 7–3 | Submit the appeal (email, portal, or certified mail). |
| 3–0 | Submit immediately. If the deadline falls on a weekend or holiday, submit the business day before. |
| 0 (past deadline) | Submit anyway with a "timely good cause" explanation. See below. |

---

## What if you miss the deadline?

You are not automatically out of luck. Most insurers and states allow an
appeal to be filed late if you can show **good cause** (also called "excusable
 neglect").

### Good cause examples:

- You were hospitalized or incapacitated during the deadline period.
- You were misinformed by an insurer representative (with notes or a recording).
- You received the EOB very late.
- You were caring for a seriously ill family member.

### What to include in a late filing:

Add a short paragraph to the top of your appeal letter:

```
Note on Timeliness: I am filing this appeal after the standard deadline due to
[reason]. I have enclosed [supporting documentation — doctor note, call log,
etc.]. I request that this appeal be accepted under the "good cause" exception.
```

> **Even with good cause, some insurers and states do not allow late filings
> for external review.** File early whenever possible.

---

## Tracking correspondence

In addition to deadlines, track every communication:

| Date sent | Method | To/from | Subject | Reference # | Date received | Notes |
|-----------|--------|---------|---------|-------------|---------------|-------|
| 2026-10-25 | Portal | Insurer | Appeal submitted | APP-9876 | 2026-10-26 | |
| 2026-11-01 | Email | Provider | Medical records request | MRQ-456 | 2026-11-05 | Records sent |

---

## Quick checklist: Before you move on

- [ ] You have identified the appeal deadline for every denied claim.
- [ ] The deadline is recorded in your tracking system (spreadsheet, calendar,
  or app).
- [ ] You have set a reminder at least 14 days before the deadline.
- [ ] You have a process for tracking all correspondence.
- [ ] You know what to do (and write) if you miss the deadline.

---

## Try it with AI

You can use AI to generate a deadline-tracking spreadsheet template, a
calendar reminder template, or a "good cause" letter paragraph. See
`docs/prompts/deadline-tracker-prompt.md` for a ready-to-use prompt.

> "I have [number] denied claims. For each, I know the EOB date and the denial
> code. Please generate: (1) a spreadsheet template with columns for claim
> number, denial date, deadline (180 days out), days remaining, status, and
> notes; (2) conditional formatting guidance to highlight overdue and
> near-deadline claims; (3) a 'good cause' letter paragraph I can adapt if I
> miss a deadline."

---

Copyright (c) 2026 Asdale Dynamics, LLC.
