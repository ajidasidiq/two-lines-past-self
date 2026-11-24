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
    lines = ENTRY.strip().splitlines()
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() for line in lines), "neither line may be blank"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back verification: what landed on disk must be exactly the entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt on disk differs from the entry"


if __name__ == "__main__":
    main()
