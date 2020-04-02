"""
1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""
import random

a = [_ for _ in range(2, 100)]
b = [_ for _ in range(2, 10)]
print(a)
print()
for value in a, b:
    if a[value] % b[value] == 0:
        print(value)