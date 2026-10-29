# Step 5: Using AI Safely and Ethically

AI is a powerful drafting assistant — but it is not a doctor, a lawyer, or an
insurance expert. This page explains how to use AI effectively while staying
safe, truthful, and within bounds.

---

## AI is a tool, not an authority

Never treat AI output as a final answer. Always verify:

| What AI produced | What you should do |
|------------------|--------------------|
| A denial-code explanation | Look it up in the insurer's official code list. |
| A quote from your plan | Check the PDF of your plan document. |
| Legal terminology | Consult your state insurance department or an attorney. |
| A deadline calculation | Confirm against the denial letter or your state regulations. |
| A medical necessity argument | Have your doctor review it. |

---

## Privacy: What to share (and what never to share)

### **NEVER share this with any AI tool:**

- Your full Social Security Number.
- Your member ID or claim numbers (mask the middle digits).
- Your full address or phone number (use a generic placeholder).
- The names of other people in your household.
- Detailed medical conditions (use codes, not descriptions, when possible).
- Bank account or payment information.

### **Safe inputs:**

- The denial code (e.g., "CO-45") and its public meaning.
- The type of service (e.g., "MRI lumbar spine without contrast").
- General timeline facts (e.g., "EOB received October 20, service date October 5").
- The structure of your argument (not the specific personal details).

### **Best practice:**

When using AI, replace personal details with placeholders:

```text
Member ID: XXXXXX[[MASKED]]
Name: [Patient]
Address: [Redacted]
```

Then fill in the real values yourself when you assemble the final letter.

---

## Using local AI (no internet, no data sharing)

If you prefer to keep everything private, you can run AI models locally on your
computer. No data leaves your machine.

### Quick setup (beginner-friendly)

| Tool | What it does | Skill level |
|------|-------------|-------------|
| **LM Studio** | Runs many open-source models locally with a friendly GUI | Beginner |
| **Ollama** | Command-line tool for downloading and running LLMs locally | Intermediate |
| **GPT4All** | Desktop app with offline models | Beginner |

### What you need

- At least 8 GB of RAM (16 GB recommended).
- At least 4 GB of free disk space for a small model (7–15 GB for larger ones).
- A modern CPU (an Apple Silicon Mac, AMD Ryzen, or Intel i5+ works fine).

### Quick start with LM Studio

1. Download LM Studio from [lmstudio.ai](https://lmstudio.ai).
2. Install and open it.
3. Browse the "Models" tab and download a lightweight model like
   `Phi-3-mini-4k-instruct` or `Llama-3-8B-Instruct`.
4. In the "Chat" tab, paste your prompt and hit send.

Local models produce slightly lower-quality output than cloud models, but for
drafting appeal letters, they are more than sufficient — and they never send
your data anywhere.

---

## Cloud AI: When and how

Cloud models (ChatGPT, Claude, Gemini) produce higher-quality text. Use them
when:

- You have stripped all personally identifiable information (PII).
- You are using a business or enterprise-tier account with a data-usage agreement
  you have read.
- You are only using the output as a draft to edit yourself.

**Never** input raw medical records, full SSNs, or claim numbers into a free
consumer AI chat.

---

## How to prompt AI for appeal-writing

The quality of AI output depends heavily on the prompt. Here is a framework:

### GOOD prompt:

> "I need to draft an insurance appeal letter. Here are the facts: [bullet
> list of facts]. The denial code is [CODE] with the meaning [description].
> I have attached [list of evidence]. Please write a professional appeal
> letter following this structure: [list the sections]. Keep the tone
> factual and respectful. Replace all personal details with placeholders
> like [Your Name]."

### BAD prompt:

> "Write an insurance appeal for me."

The bad prompt produces a generic template with no real facts. AI cannot fill
in details you never gave it.

---

## Common AI mistakes and how to catch them

| Mistake | How to catch it |
|---------|-----------------|
| **Fabricating case law** | AI sometimes cites non-existent court cases. If it mentions a specific law or case, Google it or look it up yourself. |
| **Inventing denial-code meanings** | AI may misstate what a code means. Always check the insurer's official code list. |
| **Overstating medical necessity** | AI may write that a service is "clearly medically necessary" without evidence. Tone down absolute claims. |
| **Adding fake evidence** | AI may list documents you do not actually have. Remove any attachment references that are not real. |
| **Missing the deadline** | AI may compute 180 days incorrectly. Double-check with a calendar. |

---

## Checklist: Before you send anything

- [ ] I have removed or masked all PII (SSN, full address, claim numbers).
- [ ] Every fact in the letter matches my actual documents.
- [ ] Every cited denial code is verified against the insurer's official list.
- [ ] The deadline date is calculated and confirmed by a calendar.
- [ ] My physician (if involved) has reviewed the medical-necessity language.
- [ ] I have signed the letter (physically or typed name for online submission).
- [ ] I have saved a dated copy of everything I send.

---

## Where to get help

If you need more support than AI can provide:

- **State insurance commissioner** — Free help with disputes and appeals.
- **Patient advocate** — Many hospitals have advocates who help with billing.
- **Local legal aid** — Free or low-cost legal help for healthcare-related
  issues.
- **Your provider's billing office** — They often handle appeals on your behalf.

---

Copyright (c) 2026 Asdale Dynamics, LLC.
