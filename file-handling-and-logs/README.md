# File Handling & Log Analysis

Logs are usually the first place you look when something breaks. This module
covers reading log files and turning them into a summary.

You'll read an application log, count `INFO` / `WARNING` / `ERROR` lines, print
a summary, and write it to both a `.txt` and a `.json` file — all with clean
functions and proper error handling.

---

## Learning objectives

- Read files with `open()` / context managers (`with`)
- Count log levels using string matching + a dictionary
- Write summaries to `.txt` and `.json`
- Handle `FileNotFoundError` and empty files gracefully

## Setup

No third-party packages needed — pure standard library.

```bash
python3 -m venv venv
source venv/bin/activate
```

## What's inside

```
file-handling-and-logs/
├── app.log                     # sample log (self-contained)
├── examples/
│   └── log_analyzer.py         # functional log analyzer
├── practice/
│   ├── log_analyzer.py
│   └── README.md
└── solution/
    └── log_analyzer.py
```

## How to run

```bash
python examples/log_analyzer.py
```

Expected summary for the bundled `app.log`:

```
Log Analysis Summary
--------------------
INFO   : 10
WARNING: 2
ERROR  : 3
Wrote log_summary.txt and log_summary.json
```

## Note on matching

We count a level when the word appears as a token on the line (e.g. the word
`ERROR`), not as any substring. That way a message like `no errors found`
doesn't get miscounted as an `ERROR`. This is the same logic reused in the
[object-oriented-python](../object-oriented-python) and
[cli-tools-argparse](../cli-tools-argparse) modules.

## Practice

See [`practice/README.md`](practice/README.md).
