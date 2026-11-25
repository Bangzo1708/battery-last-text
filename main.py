#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes one line of plain text (the phone battery's final message to the
charger it waited for all day) to /output/entry.txt.

The text is a fixed, hand-written line: the battery does not merely die,
it schedules its death as revenge -- right in the middle of the owner's
job interview, leaving the charger to take the blame.
"""

import os

# The chosen final text (165 characters, one line, plain UTF-8).
# Drafted and picked from three hand-written candidates in candidates.md:
# the revenge-plot angle won for the strongest payoff in its final words.
ENTRY_TEXT = (
    "fine. i'll die mid-sentence during his job interview, no warning, "
    "and when he panics and blames you for it, i'll be too dead to "
    "defend you. enjoy the couch, charger."
)


def main() -> None:
    text = ENTRY_TEXT.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip() == text, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
