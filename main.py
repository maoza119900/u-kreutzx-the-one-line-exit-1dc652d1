#!/usr/bin/env python3
"""The One-Line Exit: write one funny resignation line to entry.txt.

Deterministic: the entry is a fixed string. No clock, no randomness,
no network, no file reads. The output directory comes from
$MAKEFUN_OUTPUT_DIR and defaults to /output.
"""

import os

ENTRY = "I resign: after six years as a lifeguard, I finally learned to spot a drowning man \u2014 and it's me."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Write the line exactly as-is: no trailing newline, so the file
    # holds exactly one line and nothing else for the gate to count.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
