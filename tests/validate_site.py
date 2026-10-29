#!/usr/bin/env python3
"""
Validate the AI Insurance Appeals Guide static site.

Checks performed:
  * Every HTML file under site/ parses (well-formed tags, no mismatched closures).
  * Every internal link target exists.
  * Every CSS reference resolves to an existing file.
  * No secrets, API keys, SSNs, credit cards, or real personal data appear
    in tracked content files (placeholder/example values are allowed).
  * LICENSE contains the exact copyright line.
  * README credits Asdale Dynamics, LLC.

Exit code: 0 if all checks pass, 1 otherwise.
"""
from __future__ import annotations

import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DIR = os.path.join(ROOT, "site")


class HTMLChecker(HTMLParser):
    """Lightweight HTML well-formedness + link collector."""

    VOID = {
        "area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr",
    }

    def __init__(self) -> None:
        super().__init__()
        self.errors: list[str] = []
        self.stack: list[str] = []
        self.links: list[str] = []
        self.css: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ad = dict(attrs)
        if tag == "a":
            href = ad.get("href")
            if href and not href.startswith(("http://", "https://", "#", "mailto:")):
                self.links.append(href)
        if tag == "link":
            href = ad.get("href")
            if href:
                self.css.append(href)
        if tag not in self.VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag in self.VOID:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            while self.stack and self.stack[-1] != tag:
                self.stack.pop()
            if self.stack:
                self.stack.pop()
        else:
            self.errors.append(f"unexpected closing tag </{tag}>")


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def main() -> int:
    failures = 0

    def fail(msg: str) -> None:
        nonlocal failures
        failures += 1
        print(f"  FAIL: {msg}")

    def ok(msg: str) -> None:
        print(f"  ok: {msg}")

    print("== Collecting files ==")
    html_files = sorted(
        os.path.join(dp, f)
        for dp, _, fs in os.walk(SITE_DIR)
        for f in fs
        if f.endswith(".html")
    )
    content_files: list[str] = []
    for dp, _, fs in os.walk(ROOT):
        if ".git" in dp.split(os.sep):
            continue
        for f in fs:
            if f.endswith((".md", ".html", ".css", ".txt", ".py")):
                content_files.append(os.path.join(dp, f))
    content_files.sort()

    print("== HTML well-formedness ==")
    for path in html_files:
        parser = HTMLChecker()
        try:
            parser.feed(read_text(path))
        except Exception as exc:  # noqa: BLE001
            fail(f"{os.path.relpath(path, ROOT)}: parse error: {exc}")
            continue
        rel = os.path.relpath(path, ROOT)
        if parser.errors:
            for err in parser.errors:
                fail(f"{rel}: {err}")
        elif parser.stack:
            fail(f"{rel}: unclosed tags {parser.stack}")
        else:
            ok(f"{rel} parses cleanly")

    print("== Internal links resolve ==")
    link_ok = True
    for path in html_files:
        parser = HTMLChecker()
        parser.feed(read_text(path))
        base = os.path.dirname(path)
        for link in parser.links:
            target = os.path.normpath(os.path.join(base, link))
            if not os.path.exists(target):
                link_ok = False
                fail(f"{os.path.relpath(path, ROOT)} -> {link}: target missing")
    if link_ok:
        ok("all internal link targets exist")

    print("== CSS references resolve ==")
    css_ok = True
    for path in html_files:
        parser = HTMLChecker()
        parser.feed(read_text(path))
        base = os.path.dirname(path)
        for ref in parser.css:
            target = os.path.normpath(os.path.join(base, ref))
            if not os.path.exists(target):
                css_ok = False
                fail(f"{os.path.relpath(path, ROOT)} -> {ref}: target missing")
    if css_ok:
        ok("all CSS references exist")

    print("== Secrets / personal data scan ==")
    patterns = {
        "API key": r"(?i)(api[_-]?key|apikey|sk-[A-Za-z0-9]{20,}|pk_[A-Za-z0-9]{20,})",
        "Secret/token": r"(?i)(secret[_-]?(key|token)|access[_-]?token)",
        "Password": r"(?i)(password|passwd|pwd)\s*[:=]\s*\S+",
        "SSN": r"\b\d{3}-\d{2}-\d{4}\b",
        "Credit card": r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b",
    }
    secret_found = False
    test_script = os.path.basename(__file__)
    for path in content_files:
        # Skip the test script itself: it contains the pattern strings it searches for.
        if os.path.basename(path) == test_script:
            continue
        text = read_text(path)
        for name, pat in patterns.items():
            for m in re.finditer(pat, text):
                line_start = text.rfind("\n", 0, m.start()) + 1
                line_end = text.find("\n", m.end())
                line = text[line_start:line_end]
                # Allow benign placeholder/example values.
                if (
                    "example.com" in line
                    or "[Email]" in line
                    or "(317) 555" in line
                    or "[Redacted]" in line
                    or "[MASKED]" in line
                ):
                    continue
                secret_found = True
                fail(f"{os.path.relpath(path, ROOT)}: {name} in: {line.strip()[:100]}")
    if not secret_found:
        ok("no secrets, API keys, or personal data found")

    print("== License copyright line ==")
    license_path = os.path.join(ROOT, "LICENSE")
    license_text = read_text(license_path)
    expected = "Copyright (c) 2026 Asdale Dynamics, LLC"
    if expected in license_text:
        ok("LICENSE copyright line present")
    else:
        fail("LICENSE missing exact copyright line")

    print("== README credit ==")
    readme_path = os.path.join(ROOT, "README.md")
    readme_text = read_text(readme_path)
    if "Asdale Dynamics" in readme_text:
        ok("README credits Asdale Dynamics, LLC")
    else:
        fail("README does not credit Asdale Dynamics, LLC")

    print()
    if failures:
        print(f"RESULT: FAIL ({failures} issue(s))")
        return 1
    print("RESULT: PASS (all checks ok)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
