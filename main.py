#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — make.fun entry.

Writes one original one-line joke about office life to entry.txt and
prints exactly that line to stdout. Deterministic: no randomness, no
clock, no network, no input — every run produces the same bytes.

The grader reads /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt),
which must be UTF-8 text of 1 to 199 characters, one line.
"""

import os

JOKE = (
    "I hit reply-all to ask everyone to stop hitting reply-all, "
    "and now the whole company is hitting reply-all to agree with me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
