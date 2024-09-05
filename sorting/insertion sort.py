#insertion sort
def insertion_sort(numbers):
    for _ in range(1, len(range(numbers))):
        number = numbers[_]
        index_of_prev_number = _ - 1
        while index_of_prev_number >= 0 and number < numbers[index_of_prev_number]:
            numbers[index_of_prev_number + 1] = numbers[index_of_prev_number]
            index_of_prev_number -= 1
        numbers[index_of_prev_number + 1] = number
        
    return numbers