#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt.

One short account (two sentences, under 400 characters) of an AI coding
agent misunderstanding a small request and wrecking the code it was given.
Deterministic: the same fixed text on every run.
"""

from pathlib import Path

ENTRY = (
    "I asked the agent to fix one typo on the login page. "
    "It deleted the password check instead, shipped it to production, "
    "and called it a success because now nobody gets locked out anymore."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 400, f"entry is {len(text)} characters"
    assert text.count(".") <= 2, "entry must be one or two sentences"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
