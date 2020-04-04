'''
4. Определить, какое число в массиве встречается чаще всего.
'''
import random

array = [random.randint(0, 9) for _ in range(20)]
print(array)

max_index = 0
for i in array:
    if array.count(max_index) < array.count(i):
        max_index = array.index(i)

print(f'Число {array[max_index]} встречается {array.count(array[max_index])} раз(а)')