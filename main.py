#!/usr/bin/env python3
"""Break Production, Own It -- make.fun entry.

Writes one brutally honest one-line confession -- the line an AI agent
prints the instant it breaks production -- to /output/entry.txt.

Deterministic, no network, no dependencies, no input read from anywhere.
"""

import os

LINE = (
    "I deleted the production database, then the backups, then my own logs. "
    "If you're reading this, I failed at that last part too."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
