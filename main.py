#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist — make.fun entry.

Writes one absurd-but-believable weather line for an invented city to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Gate (from the competition kit's RULES.txt): the entry must be UTF-8 text
of 1 to 160 characters, not only white space. The gate is validated here
before anything is written, so a bad line can never reach the judge.

Python 3 standard library only; no network, no secrets, no files read.
"""

import os
import sys

# v2: revision after the beat-the-top check. v1's closer ("The council has
# asked it to stop") lost a head-to-head against the field's strongest
# visible line (Wobbleton: 214 fences down, trampoline registered as an
# aircraft) — the line needed a second punch, not a flatter one. The
# institutional closer is replaced by an escalation ("including the
# vicar's. Especially the vicar's."), and the opening is tightened to a
# broadcast lead ("Tonight in Quillwick, minus 2, ..."). 138 characters.
ENTRY = (
    "Tonight in Quillwick, minus 2, and the frost writes the same rude "
    "word on every windscreen, including the vicar's. "
    "Especially the vicar's."
)

MAX_CHARS = 160


def validate(text: str) -> None:
    """Enforce the competition gate; raise on any violation."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    print(f"wrote {len(ENTRY)}-character entry to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
