# Practice: Log Analyzer

## Your task

Complete `practice/log_analyzer.py` so that it:

1. Reads `../app.log` line by line.
2. Counts how many lines contain `INFO`, `WARNING`, and `ERROR`.
3. Prints a summary to the terminal.
4. Writes the summary to `log_summary.json`.
5. Bonus: handle the file being missing (`FileNotFoundError`) without crashing.

Expected counts for the bundled log: `INFO=10, WARNING=2, ERROR=3`.

## Run it

```bash
python practice/log_analyzer.py
```

## Done?

Compare with [`../solution/log_analyzer.py`](../solution/log_analyzer.py).
