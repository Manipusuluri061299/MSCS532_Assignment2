# MSCS-532 Assignment 2 - implementation pending

def merge_sort(values):
    """Return a new list sorted in ascending order."""
    if len(values) <= 1:
        return values.copy()

    middle = len(values) // 2

    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    sample = [38, 27, 43, 3, 9, 82, 10]
    print("Merge Sort:", merge_sort(sample))
