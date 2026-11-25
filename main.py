#!/usr/bin/env python3
"""One Line, No Deadline Met -- make.fun entry.

Writes one original one-line joke excusing a missed deadline to
/output/entry.txt. Standard library only, no network, deterministic:
the same text is written on every run.
"""

import os

ENTRY = (
    "I treated the deadline like my gym membership: "
    "I signed up full of hope in January and haven't seen it since."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the competition gate before anything is written."""
    if not text.strip():
        raise SystemExit("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    # Write atomically: a crash or a concurrent builder never leaves a
    # half-written entry behind for the grader to read.
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.replace(tmp_path, OUTPUT_PATH)
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
