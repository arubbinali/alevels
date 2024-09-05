"""
function `bubble_sort` from `sorting/bubble sort.py` (https://github.com/arubbinali/alevels/blob/main/sorting/bubble%20sort.py)
to sort the list sent to the function `binary_search` as an argument
"""
def bubble_sort(numbers):
    for _ in range(len(numbers)):
        for __ in range(len(numbers) - _ - 1):
            if numbers[__] > numbers[__ + 1]:
                numbers[__], numbers[__ + 1] = numbers[__ + 1], numbers[__]

    return numbers

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