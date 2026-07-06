# Practice: build a functional log analyzer.

import json  # noqa: F401
from pathlib import Path

LEVELS = ("INFO", "WARNING", "ERROR")
LOG_FILE = Path(__file__).parent.parent / "app.log"


def count_levels(lines):
    counts = {level: 0 for level in LEVELS}
    # TODO: increment counts[level] when a level appears.
    #       Tip: set(line.split()) then check `if level in tokens`.
    raise NotImplementedError("Implement count_levels")


def main():
    # TODO 1: read LOG_FILE lines (handle FileNotFoundError).
    # TODO 2: call count_levels(...).
    # TODO 3: print the summary.
    # TODO 4: write counts to log_summary.json with json.dump.
    pass


if __name__ == "__main__":
    main()
