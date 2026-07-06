# Practice: System Health Checker

Build your own system health script from scratch — this is the exercise that
ties the whole module together.

## Your task

Complete `practice/system_health.py` so that it:

1. Asks the user for a CPU threshold (percent) using `input()` and casts it to a number.
2. Reads the current CPU usage with `psutil.cpu_percent(interval=1)`.
3. Prints whether the CPU is healthy or over the threshold (`if / else`).
4. Bonus: also check memory (`psutil.virtual_memory().percent`) and disk (`psutil.disk_usage("/").percent`).
5. Bonus: wrap the input in `try / except ValueError` so bad input (e.g. "abc") doesn't crash the script.

## Run it

```bash
python practice/system_health.py
```

## Done?

Compare your version with [`../solution/system_health.py`](../solution/system_health.py)
and with the fuller [`../examples/system_health.py`](../examples/system_health.py).
