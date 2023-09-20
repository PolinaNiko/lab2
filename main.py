def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Ошибка! На 0 делить нельзя!")
    return a / b


def exit_program():
    exit()


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '0': exit_program
}
while True:
    operation = input("Введите операцию (+,-,*,/) или 0 для завершения программы")
    if operation not in operations:
        print("Некорректная операция. Попробуйте еще раз")
        continue
    if operation == '0':
        operations[operation]()
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = operations[operation](num1, num2)
        print("Результат:", result)
    except ValueError:
        print("Некорректный ввод числа. Попробуйте еще раз.")
    except ZeroDivisionError as e:
        print("Ошибка:", str(e))
