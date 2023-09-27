def divide_numbers(x, y):
    try:
        result = x / y
        print(f"Результат деления: {result}")

    except ZeroDivisionError:
        print("Ошибка! На ноль делить нельзя!")

    finally:
        print("Деление завершено.")

try:
    a = float(input("Введите числитель: "))
    b = float(input("Введите знаменатель: "))

    divide_numbers(a, b)

except ValueError:
    print("Ошибка! Некорректный ввод!")
finally:
    print("Программа завершена.")