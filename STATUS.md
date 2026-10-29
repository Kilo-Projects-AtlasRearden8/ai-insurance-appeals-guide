# STATUS

Built: 2026-10-29

## What was built

A beginner-friendly manual on using AI to draft insurance denial appeals and
medical bill dispute letters. Education only — not legal, medical, or billing
advice.

### File structure

```
LICENSE
README.md
STATUS.md
tests/
  validate_site.py          Reproducible verification script (HTML, links, CSS, secrets, license, readme)
docs/
  00-introduction.md        Overview and how to use this guide
  01-reading-eobs.md        Step 1: reading your Explanation of Benefits
  02-gathering-evidence.md  Step 2: collecting supporting documents
  03-writing-appeal-letters.md Step 3: drafting an appeal letter
  04-tracking-deadlines.md  Step 4: tracking filing windows
  05-using-ai-safely.md     Step 5: using AI as a drafting assistant
  06-medical-bill-disputes.md Step 6: disputing a medical bill
  prompts/
    eob-reading-prompt.md
    evidence-checklist-prompt.md
    appeal-letter-prompt.md
    dispute-letter-prompt.md
    deadline-tracker-prompt.md
site/
  index.html                Landing page (open in your browser)
  eobs.html                 Step 1: Reading EOBs
  evidence.html             Step 2: Gathering evidence
  appeals.html              Step 3: Writing appeal letters
  deadlines.html            Step 4: Tracking deadlines
  disputes.html             Step 6: Medical bill disputes
  ai-safety.html            Step 5: Using AI safely
  prompts.html              Copy-paste prompt templates (clipboard buttons)
  css/
    style.css               Shared responsive stylesheet
```

### Coverage against the goal

| Goal element | Covered? | Where |
|--------------|----------|-------|
| Read Explanation of Benefits | Yes | `docs/01-reading-eobs.md`, `site/eobs.html` |
| Gather evidence | Yes | `docs/02-gathering-evidence.md`, `site/evidence.html` |
| Write appeal letters | Yes | `docs/03-writing-appeal-letters.md`, `site/appeals.html` |
| Track deadlines | Yes | `docs/04-tracking-deadlines.md`, `site/deadlines.html` |
| Medical bill dispute letters | Yes | `docs/06-medical-bill-disputes.md`, `site/disputes.html` |
| Education only (not legal/billing advice) | Yes | Disclaimers on every page |
| Credit Asdale Dynamics, LLC | Yes | README, LICENSE, every page footer |
| MIT LICENSE (exact copyright line) | Yes | `LICENSE` |

### Credits

- **License:** MIT. Copyright line: `Copyright (c) 2026 Asdale Dynamics, LLC`
- **Created by:** Asdale Dynamics, LLC (Dylan Asdale, RN, AI author)
- **Style:** Plain English, step-by-step, never condescending — consistent with
  *The Massive AI Manual* and [dylanasdale.github.io](https://dylanasdale.github.io)

## How to run it

### Read the static site (no build step, no server required)

Open any HTML file directly in a browser:

```
open site/index.html
```

Or serve it locally:

```
cd site && python3 -m http.server 8000
# then open http://localhost:8000
```

### Read the markdown docs

Open any file in `docs/` with a markdown viewer (VS Code, Obsidian, GitHub, etc.).

### Use the AI prompts

Copy a prompt from `docs/prompts/` (or the "AI Prompts" page), paste it into
your AI tool, and replace the bracketed placeholders with your own facts. Mask
all personal details (SSN, member ID, claim numbers) before sharing with any AI.

### Run the verification tests

```
python3 tests/validate_site.py
```

Expected output: `RESULT: PASS (all checks ok)` and exit code 0.

## Verification results

All checks passed on 2026-10-29 via `tests/validate_site.py`:

| Check | Result |
|-------|--------|
| HTML well-formedness (all 8 pages) | PASS — no unclosed or mismatched tags |
| Internal links (navigation + cross-references) | PASS — all targets resolve |
| CSS references | PASS — `css/style.css` exists and is referenced by every page |
| HTTP server (all 8 pages + CSS) | PASS — HTTP 200, all pages > 1 KB |
| Secrets / personal data scan | PASS — no API keys, passwords, SSNs, cards, or real personal data |
| LICENSE copyright line | PASS — exactly `Copyright (c) 2026 Asdale Dynamics, LLC` |
| README credit | PASS — Asdale Dynamics, LLC credited; copyright line present |
| No `.github/workflows` files | PASS — none created |
| No remote repos or pushes | PASS — local only |
| Git commit | PASS — committed as `Dylan Asdale` / `dylanasdale@users.noreply.github.com` |

## Known gaps

- **Not legal/billing advice.** Every insurance plan and provider is different.
  Users must verify deadlines, denial codes, coverage, and billing amounts
  against their own plan documents and state regulations.
- **Denial-code meanings** are illustrative, not exhaustive. Users should check
  the insurer's official code list for authoritative meanings.
- **Deadline calculations** assume 180 days from the EOB date, which is common
  but not universal. Some plans and states use different windows.
- **AI output is a first draft.** The guide explicitly instructs users to verify
  every fact, remove placeholders, and have a physician review
  medical-necessity language before sending.
- **Local AI setup** is described at a high level. Specific hardware
  requirements and model choices vary; the guide points to tools (LM Studio,
  Ollama, GPT4All) rather than providing a step-by-step install guide.
- **No interactive tools.** This is a static site and documentation set. No
  prompt-running interface, no spreadsheet generator, and no deadline tracker
  app is included — only templates and guidance for using external tools.
- **No state-specific content.** Appeal rules vary by state; this guide covers
  general U.S. processes.

## Commit history

```
<latest> Add medical bill disputes step, improved README, and validation tests
<prev>   Add AI insurance appeals beginner manual: docs, static site, prompts, and license
```

Plain commit messages, no Co-authored-by trailers. Local repository only — no
remote, no push.