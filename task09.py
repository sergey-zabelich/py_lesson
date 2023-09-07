'''Задача НЕГАФИБОНАЧЧИ по желанию
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
'''
def findFib(index):
    if index == 1:
        return 0
    elif index == 2:
        return 1
    return findFib(index-1) + findFib(index-2)

n = int(input("Введите число: "))

# Получение списка положительных чисел Фибоначчи
positive_sequence = [findFib(i) for i in range(1, n+2)]

# Получение списка отрицательных чисел Фибоначчи
negative_sequence = [findFib(i) if i % 2 == 0 else -findFib(i) for i in range(1, n+2)]

# Объединение списков положительных и отрицательных чисел в один список
lst = negative_sequence[::-1] + positive_sequence[1:]

print("Отрицательные и положительные числа Фибоначчи:")
print(lst)