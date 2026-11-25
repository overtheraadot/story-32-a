#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters entry (account A).

Writes one Wi-Fi network name, 23 characters, to /output/entry.txt.
Deterministic, stdlib only, no network, no secrets.

The joke: Dad sold the router for beer. One name implies a whole
situation (a house with no Wi-Fi), a character (Dad), and an event
(the sale) — the reader fills in the rest: the family staring at a
dead network, Dad shrugging, the beer already gone. It dodges the
stock Wi-Fi jokes (no FBI van, no "pretty fly for a Wi-Fi") and stays
tight: every character earns its place.
"""

import os

# The story: Dad sold the router for beer — and the house has had no
# Wi-Fi since. Character, event and situation in 23 characters.
STORY = "DadSoldTheRouterForBeer"

MAX_CHARS = 32
OUT_PATH = "/output/entry.txt"


def verify(text: str) -> str:
    """Return the name, stripped, after enforcing the gate.

    Mirrors the sealed scorer: UTF-8 text of 1 to 32 characters, and
    not only white space.
    """
    line = text.strip()
    if not line:
        raise ValueError("entry is empty or only white space")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, must be at most {MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def write_entry(text: str, path: str = OUT_PATH) -> str:
    """Verify the entry and write it to the output file."""
    line = verify(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(path, 0o644)
    return line


def main() -> None:
    line = write_entry(STORY)
    print(f"Wrote {len(line)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
