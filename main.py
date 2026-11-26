#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes one original one-line office joke to /output/entry.txt.
Deterministic: the joke is a fixed literal, no randomness, no clock,
no network, no input files.

The joke's shape: setup (a company-wide email begging people to stop
hitting reply-all) + turn (the plea itself triggers a reply-all storm)
+ punchline last (they are all replying-all to agree with it).
No trailing newline is written: the gate counts characters, and a
newline would add a character plus an empty second line.
"""

import os

JOKE = (
    "I sent a company-wide email asking everyone to stop hitting "
    "reply-all, and now 400 people are replying-all to agree with me."
)


def main() -> None:
    text = JOKE
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    assert text.strip() == text and text.strip(), "joke must not be blank"
    assert "\n" not in text and "\r" not in text, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back what was written and verify it byte-for-byte.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "written output differs from the joke"
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
