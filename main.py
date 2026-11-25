"""One Line, No Deadline Met.

Writes a single-line joke giving an excuse for a missed deadline
to <output dir>/entry.txt. The output directory comes from the
MAKEFUN_OUTPUT_DIR environment variable and defaults to /output,
which is where the make.fun program/v1 harness expects the entry.
Standard library only, no network, fully deterministic.
"""

import os
from pathlib import Path

# The entry: one sentence, one excuse, punch at the end.
ENTRY = (
    "I didn't miss the deadline, I just gave it a head start "
    "so it could enjoy being early for once."
)


def main() -> None:
    # Self-check the gate before writing: one line, 1-200 characters,
    # real text rather than whitespace, so a bad edit can never ship
    # an entry the scorer would mark invalid.
    if not (1 <= len(ENTRY) <= 200):
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-200")
    if "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be a single non-blank line")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
