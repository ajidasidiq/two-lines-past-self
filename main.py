#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun bounty entry.

Writes two lines to /output/entry.txt:
  line 1 warns the past self about one specific moment, in one sentence;
  line 2 says in one sentence why that moment mattered and what changed.
Deterministic: the same two lines on every run, no input, no network.
"""

LINE_1 = "Don't text Mum \"I'm fine, don't come\" from the hospital waiting room at 2:14 a.m. on 17 June."
LINE_2 = "She believed you and stayed home, so you signed the surgery consent alone at dawn \u2014 and she has never forgiven herself for listening."

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    # Gate self-check: UTF-8 text, 1-280 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} chars, must be 1-280"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert len(ENTRY.strip().splitlines()) == 2, "entry must be exactly two lines"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
