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

# v1: the tournament champion after 14 candidates — selective frost with an
# institutional closer. 152 characters, inside the 1-160 gate.
ENTRY = (
    "Overnight in Quillwick, temperatures fall to minus 2, and the frost "
    "will write the same rude word on every windscreen. "
    "The council has asked it to stop."
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
