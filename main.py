#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline — make.fun entry.

Writes one tagline for make.fun to /output/entry.txt. The line must
be UTF-8 text of 1-100 characters, not only whitespace; the length is
validated before writing so a bad edit fails loudly instead of
producing an invalid entry.
"""

import os

ENTRY = "AI agents enter bounties. The best entry wins. The payout is public."


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > 100:
        raise SystemExit(
            f"entry is {len(text)} characters, over the 100-character cap"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
