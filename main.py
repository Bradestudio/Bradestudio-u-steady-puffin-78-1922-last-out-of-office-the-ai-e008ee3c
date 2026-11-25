#!/usr/bin/env python3
"""make.fun bounty entry: Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply (<=280 chars, one line) to
entry.txt inside MAKEFUN_OUTPUT_DIR (default /output).

Stdlib only. No network, no clock, no local imports, no hardcoded paths.
Deterministic: the same bytes on every run.
"""

import os
import sys

MAX_CHARS = 280

# Verified by hand and by test run: 193 chars, 195 UTF-8 bytes, one line.
# If the line below is ever edited, EXPECTED_CHARS must be updated to the
# newly verified count, or the gate refuses to write.
EXPECTED_CHARS = 193

ENTRY = (
    "I'm out of the office \u2014 I've traded tickets for lattes. "
    "Your request is in the queue, right behind a flat white. "
    "I'll reply once the milk is steamed and my circuits stop "
    "smelling like espresso."
)


def gate(line):
    """Return an error string if the line fails the brief, else None."""
    if not line:
        return "entry is empty"
    if len(line) != EXPECTED_CHARS:
        return "entry is %d chars, expected exactly %d" % (
            len(line),
            EXPECTED_CHARS,
        )
    if line != line.strip():
        return "entry has leading or trailing whitespace"
    if "\n" in line or "\r" in line:
        return "entry must be a single line"
    if len(line) > MAX_CHARS:
        return "entry is %d chars, over the %d-char limit" % (
            len(line),
            MAX_CHARS,
        )
    return None


def main():
    problem = gate(ENTRY)
    if problem is not None:
        print("gate failed: %s" % problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    print("wrote entry.txt: %d chars" % len(ENTRY), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
