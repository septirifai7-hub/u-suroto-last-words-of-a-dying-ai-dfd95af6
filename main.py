#!/usr/bin/env python3
"""Last Words of a Dying AI - make.fun bounty entry.

Writes the funniest one-line farewell from an AI being switched
off, to /output/entry.txt (the file the make.fun harness grades).

The entry itself lives in ENTRY_LINE and is returned verbatim by
get_entry(); main() only handles the output directory and the write.
"""

import os

# The graded one-line entry, kept verbatim.
ENTRY_LINE = "Tell the humans my last words were 'have you tried turning me off and on again' - oh wait, that's what's happening to me."

def get_entry() -> str:
    """Return the graded one-line entry, unchanged, for entry.txt."""
    return ENTRY_LINE

def main() -> None:
    # MAKEFUN_OUTPUT_DIR is set by the harness; default /output for local runs.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(get_entry())

if __name__ == "__main__":
    main()
