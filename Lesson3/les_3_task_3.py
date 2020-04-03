"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

array = [random.randint(0, 99) for _ in range(10)]
print(f'Исходный масив:\n{array}')

max = array[0]
min = array[0]

for i in array:
    if i > max:
        max = i
    elif i < min:
        min = i
min_index = array.index(min)
max_index = array.index(max)
array[min_index], array[max_index] = array[max_index], array[min_index]
print(f'Измененный масив:\n{array}')