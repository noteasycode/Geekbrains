'''
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
'''
import random

array = [random.randint(-99, 99) for _ in range(20)]
print(f'Массив: {array}')

min_index = 0

for i in array:
    if array[min_index] > i:
        min_index = array.index(i)

if array[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'Максимальный отрицательный элемент: {array[min_index]}.',
            f'Позиция в массиве: {min_index}')