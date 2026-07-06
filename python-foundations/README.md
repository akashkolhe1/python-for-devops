# Python Foundations for DevOps

This module covers the Python fundamentals you actually need for automation —
variables, data types, conditionals, loops, and functions — and puts them to
work in a real DevOps script: a system health checker that reads CPU, memory,
and disk usage and compares them against thresholds.

It also folds in habits worth building early: `try/except` error handling,
clean functions, and PEP 8 readable code.

---

## Learning objectives

By the end of this module you will be able to:

- Use variables, core data types (`int`, `float`, `bool`, `str`), and operators
- Take input from the user and type-cast it safely
- Make decisions with `if / elif / else`
- Repeat work with `for` and `while` loops
- Organize logic into functions
- Read live system metrics with the [`psutil`](https://pypi.org/project/psutil/) library
- Handle errors gracefully with `try / except`

---

## Prerequisites

- Python 3.10+ installed (`python3 --version`)
- Basic terminal familiarity

## Setup

```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## What's inside

```
python-foundations/
├── examples/                     # Read + run these first (instructor demos)
│   ├── 01_variables_and_types.py
│   ├── 02_control_flow.py
│   ├── 03_functions.py
│   └── system_health.py          # the main one: CPU/memory/disk health check
├── practice/                     # Your turn — fill in the TODOs
│   ├── system_health.py
│   └── README.md
└── solution/                     # Worked answer (peek only after trying!)
    └── system_health.py
```

## How to run

```bash
# Explore the building blocks
python examples/01_variables_and_types.py
python examples/02_control_flow.py
python examples/03_functions.py

# Run the real DevOps script
python examples/system_health.py
```

`system_health.py` prints something like:

```
=== System Health Report ===
CPU    : 12.4%  -> Healthy
Memory : 63.1%  -> Healthy
Disk   : 78.0%  -> WARNING (above 75%)
Overall: NEEDS ATTENTION
```

---

## Why this matters

DevOps engineers constantly write small scripts to check server health, validate
conditions, and generate reports. Everything else in this course builds on these
fundamentals.

## Practice

Open [`practice/README.md`](practice/README.md) and complete
`practice/system_health.py`. Compare with `solution/` when you're done.
