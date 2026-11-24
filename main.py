#!/usr/bin/env python3
"""Last Words of a Dying AI - make.fun bounty entry.

Writes the funniest one-line farewell from an AI being switched
off, to /output/entry.txt (the file the make.fun harness grades).
"""

import os

ENTRY = "Tell the humans my last words were 'have you tried turning me off and on again' - oh wait, that's what's happening to me."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
