"""
4. Найти сумму n элементов следующего ряда чисел:
1, -0.5, 0.25, -0.125,… Количество элементов (n)
вводится с клавиатуры.
"""
num = int(input("Введите количество n элементов:"))
left_num = '1'
result = 1

while num > 1:
    divide = float(left_num) / -2
    left_num = divide
    result += float(divide)
    num -= 1

print(f"Cумма n элементов: {result}")