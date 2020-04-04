'''
6. В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''
import random

array = [random.randint(0, 99) for _ in range(10)]
print(array)

min_index = 0
max_index = 0
step = 1
sum = 0

for i in array:
    if array[min_index] > i:
        min_index = array.index(i)
    elif array[max_index] < i:
        max_index = array.index(i)

if max_index - min_index < 0:
    step = -1

for i in array[min_index + step:max_index:step]:
    sum += i

print(f'Сумма элементов между минимальным {array[min_index]} '
      f'и максимальным {array[max_index]} элементами составляет: {sum}')