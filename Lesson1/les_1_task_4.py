"""
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят,
и сколько между ними находится букв
"""

a = ord(input('Вводим первую букву:'))
b = ord(input('Вводим вторую букву:'))
a = a - ord('a') + 1
b = b - ord('a') + 1
print(f"Позиция первой буквы: {a}")
print(f"Позиция второй буквы: {b}")
print(f"К-во букв между символами:' {abs(a-b)-1}")
