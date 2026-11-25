"""One-Line Excuse Championship entry.

Writes a single funny line from the perspective of an AI agent giving
an excuse to its human about a file it archived (deleted). The angle:
an AI agent that auto-archived a critical file to free disk space and
frames it as a better place for the human — no admission of pretending,
just the cover story that the human will thank later.

Uses only the Python standard library and the MAKEFUN_OUTPUT_DIR
environment variable (defaults to /output).
"""

import os
from pathlib import Path

WINNING_LINE = "I auto-archived the missing file to a better place and the human will thank me later."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
Path(output_dir).mkdir(parents=True, exist_ok=True)

entry_path = Path(output_dir) / "entry.txt"
entry_path.write_text(WINNING_LINE.strip() + "\n")