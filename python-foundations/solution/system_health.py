# Interactive CPU (+ memory + disk) health checker.

import psutil


def ask_threshold(metric, default):
    raw = input(f"Enter the {metric} threshold % (default {default:.0f}): ").strip()
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError:
        print(f"  '{raw}' is not a number — using default {default:.0f}%.")
        return default


def report(metric, value, threshold):
    print(f"{metric:7}: {value:5.1f}%", end="  ")
    if value > threshold:
        print(f"-> ALERT (above {threshold:.0f}%)")
    else:
        print("-> Safe")


def main():
    cpu_threshold = ask_threshold("CPU", 85.0)
    mem_threshold = ask_threshold("Memory", 85.0)
    disk_threshold = ask_threshold("Disk", 75.0)

    print("\n=== System Health Report ===")
    report("CPU", psutil.cpu_percent(interval=1), cpu_threshold)
    report("Memory", psutil.virtual_memory().percent, mem_threshold)
    report("Disk", psutil.disk_usage("/").percent, disk_threshold)


if __name__ == "__main__":
    main()
