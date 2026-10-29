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
docs/
  00-introduction.md          Overview, appeal process, educational disclaimer
  01-reading-eobs.md          How to read an EOB, denial codes (CO/PR/RP)
  02-gathering-evidence.md    Medical records, physician statements, prior auth
  03-writing-appeal-letters.md 11-part letter structure + AI drafting workflow
  04-tracking-deadlines.md    Deadline types, tracking systems, good-cause filings
  05-using-ai-safely.md       Privacy, local AI, prompt quality, common mistakes
  prompts/
    eob-reading-prompt.md
    evidence-checklist-prompt.md
    appeal-letter-prompt.md
    dispute-letter-prompt.md
    deadline-tracker-prompt.md
site/
  index.html                 Landing page with overview + link cards
  eobs.html                  Step 1: Reading EOBs
  evidence.html              Step 2: Gathering evidence
  appeals.html               Step 3: Writing appeal letters
  deadlines.html             Step 4: Tracking deadlines
  ai-safety.html             Step 5: Using AI safely
  prompts.html               Copy-paste prompt templates (with clipboard buttons)
  css/style.css              Shared stylesheet (responsive, accessible)
```

### Credits

- **License:** MIT. Copyright line: `Copyright (c) 2026 Asdale Dynamics, LLC`
- **Created by:** Asdale Dynamics, LLC (Dylan Asdale, RN, AI author)
- **Style:** Plain English, step-by-step, never condescending — consistent with
  *The Massive AI Manual* and [dylanasdale.github.io](https://dylanasdale.github.io)

## How to run it

### Read the site (no build step, no server required)

Open any HTML file directly in a browser:

```
open site/index.html
```

Or serve it locally with a static server:

```
cd site && python3 -m http.server 8000
# then open http://localhost:8000
```

### Read the markdown docs

Open any file in `docs/` with a markdown viewer (VS Code, Obsidian, GitHub, etc.).

### Use the AI prompts

Copy the prompt from `docs/prompts/` or from the "AI Prompts" page in the site,
paste it into your AI tool, and replace the bracketed placeholders with your own
facts. Mask all personal details (SSN, member ID, claim numbers) before sharing
with any AI.

## Verification results

All checks passed on 2026-10-29:

| Check | Result |
|-------|--------|
| HTML parse (all 7 pages) | PASS — no unclosed tags, no mismatched tags |
| Internal links (navigation + cross-references) | PASS — all targets resolve |
| CSS references | PASS — `css/style.css` exists and is referenced by every page |
| HTTP server (all 7 pages + CSS) | PASS — HTTP 200, all pages > 1 KB |
| CSS brace balance | PASS — 66 open / 66 close |
| Secrets scan (API keys, passwords, SSNs, cards, emails, phones) | PASS — no secrets, API keys, or personal data |
| LICENSE copyright line | PASS — exactly `Copyright (c) 2026 Asdale Dynamics, LLC` |
| README credit | PASS — Asdale Dynamics, LLC credited; copyright line present |
| Git commit | PASS — 21 files committed as `Dylan Asdale` / `dylanasdale@users.noreply.github.com` |
| No `.github/workflows` files | PASS — none created |
| No remote repos or pushes | PASS — local only |

## Known gaps

- **Not legal/billing advice.** Every insurance plan is different. Users must
  verify deadlines, denial codes, and coverage against their own plan documents
  and state regulations.
- **Denial-code meanings** are illustrative, not exhaustive. Users should check
  the insurer's official code list for authoritative meanings.
- **Deadline calculations** assume 180 days from the EOB date, which is common
  but not universal. Some plans and states use different windows.
- **AI output is a first draft.** The guide explicitly instructs users to verify
  every fact, remove placeholders, and have a physician review medical-necessity
  language before sending.
- **Local AI setup** is described at a high level. Specific hardware requirements
  and model choices vary; the guide points to tools (LM Studio, Ollama, GPT4All)
  rather than providing a step-by-step install guide.
- **No interactive tools.** This is a static site and documentation set. No
  prompt-running interface, no spreadsheet generator, and no deadline tracker
  app is included — only templates and guidance for using external tools.
- **No state-specific content.** Appeal rules vary by state; this guide covers
  general U.S. processes.

## Commit history

```
e9d036e Add AI insurance appeals beginner manual: docs, static site, prompts, and license
```

Plain commit messages, no Co-authored-by trailers. Local repository only — no
remote, no push.