import json
from pathlib import Path

LEVELS = ("INFO", "WARNING", "ERROR")
LOG_FILE = Path(__file__).parent.parent / "app.log"
OUTPUT = Path(__file__).parent / "log_summary.json"


def read_lines(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Log file not found: {path}")
        return []


def count_levels(lines):
    counts = {level: 0 for level in LEVELS}
    for line in lines:
        tokens = set(line.split())
        for level in LEVELS:
            if level in tokens:
                counts[level] += 1
    return counts


def main():
    lines = read_lines(LOG_FILE)
    if not lines:
        print("No logs to analyze.")
        return

    counts = count_levels(lines)
    for level in LEVELS:
        print(f"{level:7}: {counts[level]}")

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(counts, f, indent=2)
    print(f"Wrote {OUTPUT.name}")


if __name__ == "__main__":
    main()
