"""Write one fixed one-liner about everyday life to /output/entry.txt.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The program is deterministic: it writes the same bytes on every run.
Standard library only; no network.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = "Folding a fitted sheet is my weekly reminder that confidence is not competence."


def main() -> None:
    out = Path(OUTPUT_DIR) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
