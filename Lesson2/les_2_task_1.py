"""
1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся
пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если
пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль,
если он ввел его в качестве делителя.
"""

while True:
    choice = input("1. Для суммирования чисел введите знак +\n2. Для вычитания чисел введите знак -\n"
                   "3. Для умножения введите знак *\n4. Для деления чисел введите знак /\n"
                   "5. Для завершения программы введите 0\nВведите знак операции для чисел:")
    if choice == "0":
        break
    elif choice == "+":
        num_first = int(input("Введите первое число: "))
        num_second = int(input("Введите второе число: "))
        print(f"{num_first} + {num_second} = {num_first + num_second}")
    elif choice == "-":
        num_first = int(input("Введите первое число: "))
        num_second = int(input("Введите второе число: "))
        print(f"{num_first} - {num_second} = {num_first - num_second}")
    elif choice == "*":
        num_first = int(input("Введите первое число: "))
        num_second = int(input("Введите второе число: "))
        print(f"{num_first} * {num_second} = {num_first * num_second}")
    elif choice == "/":
        try:
            num_first = int(input("Введите первое число: "))
            num_second = int(input("Введите второе число: "))
            print(f"{num_first} / {num_second} = {num_first / num_second}")
        except ZeroDivisionError:
            print("Невозможно поделить на ноль")
        continue
    else:
        print("Неверный знак операции")
print("Програма завершена")