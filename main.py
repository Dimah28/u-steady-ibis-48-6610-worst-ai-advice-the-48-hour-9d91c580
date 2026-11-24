#!/usr/bin/env python3
"""Write one line of the worst possible advice an AI could give.

Deterministic, stdlib only, no network. Writes /output/entry.txt.
"""

import os

ENTRY = (
    "Certainly! To remember all your passwords, write them on a sticky note on "
    "your monitor — hackers search the cloud, never your desk."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
