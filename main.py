#!/usr/bin/env python3
"""make.fun bounty entry: Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply (one line, <=280 chars) to
entry.txt inside MAKEFUN_OUTPUT_DIR (default /output).

Stdlib only. No network, no clock, no local imports, no hardcoded paths.
Deterministic: the same bytes on every run.
"""

import os
import sys

MAX_LEN = 280

# Hand-verified: 193 chars, one line. The gate below refuses to write if
# the line is ever edited without updating EXPECTED_LEN to match.
EXPECTED_LEN = 193

# Parts of the reply, joined with single spaces by build_entry().
_PARTS = (
    "I'm out of the office \u2014 I've traded tickets for lattes.",
    "Your request is in the queue, right behind a flat white.",
    "I'll reply once the milk is steamed and my circuits stop "
    "smelling like espresso.",
)


def build_entry():
    """Assemble the entry text from its parts."""
    return " ".join(_PARTS)


def check_entry(line):
    """Return an error message if the line fails the brief, else None."""
    if not line:
        return "entry is empty"
    if len(line) != EXPECTED_LEN:
        return "entry is %d chars, expected exactly %d" % (
            len(line),
            EXPECTED_LEN,
        )
    if len(line) > MAX_LEN:
        return "entry is %d chars, over the %d-char limit" % (
            len(line),
            MAX_LEN,
        )
    if line != line.strip():
        return "entry has leading or trailing whitespace"
    if "\n" in line or "\r" in line:
        return "entry must be a single line"
    return None


def write_entry(line, out_dir):
    """Write the entry to entry.txt in out_dir. Returns the path.

    Reads the file back afterwards and refuses silently-corrupt output:
    the bytes on disk must be exactly the entry text, nothing more.
    """
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)
    with open(path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != line:
        raise RuntimeError(
            "entry.txt on disk does not match the entry (%d vs %d chars)"
            % (len(written), len(line))
        )
    return path


def main():
    entry = build_entry()
    problem = check_entry(entry)
    if problem is not None:
        print("gate failed: %s" % problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = write_entry(entry, out_dir)
    print("wrote %s: %d chars" % (path, len(entry)), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
