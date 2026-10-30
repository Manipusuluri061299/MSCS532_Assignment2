# MSCS-532 Assignment 2 

import random

from merge_sort import merge_sort
from quick_sort import quick_sort


def run_tests():
    random_generator = random.Random(42)

    cases = {
        "Empty": [],
        "Single": [7],
        "Already sorted": [1, 2, 3, 4, 5],
        "Reverse sorted": [5, 4, 3, 2, 1],
        "Duplicates": [5, 2, 5, 3, 2],
        "Negative values": [-4, 8, -1, 0, 3],
        "Random dataset": [
            random_generator.randint(-100, 100)
            for _ in range(100)
        ],
    }

    algorithms = {
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
    }

    for algorithm_name, algorithm in algorithms.items():
        for case_name, data in cases.items():
            original = data.copy()
            expected = sorted(data)
            actual = algorithm(data)

            assert actual == expected, (
                f"{algorithm_name} failed {case_name}"
            )
            assert data == original, "Input was modified"

            print(f"PASS: {algorithm_name} - {case_name}")

    print("\nAll 14 tests passed!")


if __name__ == "__main__":
    run_tests()
