"""
1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""

a = [_ for _ in range(2, 100)]
b = [_ for _ in range(2, 10)]
result = [0]*8

for i in a:
    for j in b:
        if i % j == 0:
            result[j-2] += 1
print(result)

i = 0
while i < len(result):
    print(f"{i+2} | {result[i]}")
    i += 1