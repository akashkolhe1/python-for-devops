# Practice: finish the TODOs to build a CPU health checker.

import psutil


def check_cpu_threshold():
    # TODO 1: ask for a CPU threshold and cast it to an int
    #         cpu_threshold = ...
    raise NotImplementedError("Remove this line and implement the function")

    # TODO 2: read current CPU usage -> psutil.cpu_percent(interval=1)
    # TODO 3: print the current CPU usage
    # TODO 4: if current_cpu > cpu_threshold print an alert, else print it's safe

    # BONUS: wrap TODO 1 in try/except ValueError for bad input
    # BONUS: also check memory and disk


if __name__ == "__main__":
    check_cpu_threshold()
