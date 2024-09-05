#binary search
def binary_search(unsorted_numbers, number):
    numbers = bubble_sort(unsorted_numbers)
    low, high = 0, len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == number:
            return f"{number} is at index {mid} in the list"
        elif numbers[mid] > number:
            high = mid - 1
        else:
            low = mid + 1

    return f"{number} is not in the list"