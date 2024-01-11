def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers
numbers = [4, 6, 2, 9, 7]
sorted_numbers = sort_list_imperative(numbers)
print(sorted_numbers)  # Выводит: [9, 7, 6, 4, 2]