def sort_list_declarative(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers

# Пример использования
numbers = [4, 6, 2, 9, 7]
sorted_numbers = sort_list_declarative(numbers)
print(sorted_numbers)  # Выводит: [9, 7, 6, 4, 2]