"""Fortune in a Pot — one kind, funny fortune for the houseplant on the sill.

The program prints a single fortune-cookie line for a houseplant to
``entry.txt`` inside the output directory make.fun provides. The text is
fixed: the joke is the whole entry, so there is nothing to compute, only
something to deliver exactly as written, with no trailing newline.
"""

import os
import sys

FORTUNE = (
    "Soon the postman will wave at you through the glass, "
    "and your keeper will swear the whole street knows your name."
)

GATE_MIN = 1
GATE_MAX = 120


def resolve_output_path():
    """Return the entry.txt path, honouring the grader's output dir."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def validate(text):
    """Check the fortune against the competition's gate before writing."""
    if not isinstance(text, str):
        raise TypeError("fortune must be text")
    if not GATE_MIN <= len(text) <= GATE_MAX:
        raise ValueError("fortune must be 1 to 120 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("fortune must not be only whitespace")
    return text


def main():
    fortune = validate(FORTUNE)
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(fortune)
    # Post-write guard: re-read and confirm the file holds exactly the
    # fortune we validated, byte for byte, with nothing appended.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != fortune.encode("utf-8"):
        raise ValueError("entry.txt does not match the validated fortune")
    return 0


if __name__ == "__main__":
    sys.exit(main())
