"""
Вводятся три разных числа.
Найти, какое из них является средним
(больше одного, но меньше другого)
"""

print('Введите три числа: ')
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if b < a < c or c < a < b:
    print('Среднее число:', a)
elif a < b < c or c < b < a:
    print('Среднее число:', b)
else:
    print('Среднее число:', c)