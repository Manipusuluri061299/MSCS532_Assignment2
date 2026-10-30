# MSCS-532 Assignment 2 

def quick_sort(values):
    """Return a new list sorted using randomized-style
    balanced partitioning with a median-of-three pivot.
    """
    if len(values) <= 1:
        return values.copy()

    first = values[0]
    middle = values[len(values) // 2]
    last = values[-1]

    pivot = sorted((first, middle, last))[1]

    smaller = []
    equal = []
    larger = []

    for value in values:
        if value < pivot:
            smaller.append(value)
        elif value > pivot:
            larger.append(value)
        else:
            equal.append(value)

    return quick_sort(smaller) + equal + quick_sort(larger)


if __name__ == "__main__":
    sample = [38, 27, 43, 3, 9, 82, 10]
    print("Quick Sort:", quick_sort(sample))
