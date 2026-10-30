# MSCS-532 Assignment 2

import csv
import gc
import random
import statistics
import time
import tracemalloc

from merge_sort import merge_sort
from quick_sort import quick_sort


SIZES = [100, 1000, 5000, 10000]
REPEATS = 5


def create_dataset(size, dataset_type):
    if dataset_type == "sorted":
        return list(range(size))

    if dataset_type == "reverse":
        return list(range(size, 0, -1))

    if dataset_type == "random":
        generator = random.Random(42 + size)
        return [generator.randint(0, size * 10)
                for _ in range(size)]

    raise ValueError("Unknown dataset type")


def measure(algorithm, data):
    # Time measurements exclude the separate memory probe.
    durations = []

    for _ in range(REPEATS):
        gc.collect()
        start = time.perf_counter()
        result = algorithm(data.copy())
        duration = time.perf_counter() - start

        assert result == sorted(data)
        durations.append(duration * 1000)

    # Measure peak Python-tracked memory separately.
    gc.collect()
    tracemalloc.start()
    tracemalloc.reset_peak()

    result = algorithm(data.copy())
    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()
    assert result == sorted(data)

    return (
        statistics.median(durations),
        peak / 1024,
    )


def main():
    algorithms = {
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
    }

    rows = []

    for size in SIZES:
        for dataset_type in ("sorted", "reverse", "random"):
            data = create_dataset(size, dataset_type)

            for name, algorithm in algorithms.items():
                elapsed_ms, peak_kib = measure(algorithm, data)

                row = {
                    "algorithm": name,
                    "size": size,
                    "dataset": dataset_type,
                    "median_time_ms": round(elapsed_ms, 4),
                    "peak_traced_kib": round(peak_kib, 2),
                }

                rows.append(row)
                print(row)

    with open(
        "benchmark_results.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=rows[0].keys(),
        )
        writer.writeheader()
        writer.writerows(rows)

    print("\nBenchmark completed.")
    print("Results saved to benchmark_results.csv")


if __name__ == "__main__":
    main()
