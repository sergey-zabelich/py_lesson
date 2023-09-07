'''
Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.Каждое число вводится с новой строки.
'''
def find_indexes(lst, min_value, max_value):
    indexes = []
    for i in range(len(lst)):
        if min_value <= lst[i] <= max_value:
            indexes.append(i)
    return indexes
lst = [1, 5, 88, 100, 2, -4]
min_value = 33
max_value = 200
result = find_indexes(lst, min_value, max_value)
print(result)
