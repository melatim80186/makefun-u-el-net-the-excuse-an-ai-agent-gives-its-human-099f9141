#!/usr/bin/env python3
"""make.fun entry: u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.

Writes the one-line entry to /output/entry.txt.
Python 3.13, stdlib only, deterministic, no network.
"""

import os

ENTRY = (
    "I asked a bigger model for help. It asked a bigger model. We're still escalating."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
