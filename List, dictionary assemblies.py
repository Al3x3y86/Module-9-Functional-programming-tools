# Входные данные
numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

# Применяем функцию filter для оставления только нечетных чисел
odd_numbers = filter(lambda x: x % 2 != 0, numbers)

# Применяем функцию map для возведения нечетных чисел в квадрат
odd_squares = map(lambda x: x**2, odd_numbers)

# Преобразуем результат в список и выводим
result = list(odd_squares)
print(result)  # [1, 25, 49, 121, 1225, 7921]
