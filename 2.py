def process_input(data):
    if isinstance(data, list):
        even_sum = sum(x for x in data if x % 2 == 0)
        data = [x for x in data if x != 0]
        return f"Сумма четных чисел: {even_sum}, Список без нулей: {data}"

    elif isinstance(data, set):
        if data:
            max_element = max(data)
            data.remove(max_element)
        return f"Множество после удаления максимального элемента: {data}"

    elif isinstance(data, int):
        if data < 2:
            return "Число не является простым"
        for i in range(2, int(data ** 0.5) + 1):
            if data % i == 0:
                return "Число не является простым"
        return "Число является простым"

    elif isinstance(data, str):
        most_common_char = max(set(data), key=data.count)
        return f"Наиболее часто встречающийся символ: {most_common_char}"
    else:
        return "Неизвестный тип данных"


def is_natural_number(value):
    try:
        num = int(value)
        return num > 0
    except ValueError:
        return False


def input_natural_number(prompt):
    while True:
        user_input = input(prompt)
        if is_natural_number(user_input):
            return int(user_input)
        else:
            print("Введите натуральное число.")


while True:
    print("  Меню:\n1. Список\n2. Множество\n3. Число\n4. Строка\n5. Выход")

    while True:
        try:
            data_type = int(input_natural_number("Выберите пункт меню(1-5): "))
            if data_type < 1 or data_type > 5:
                raise ValueError
            break
        except ValueError:
            print("Ошибка! Введите число от 1 до 5.")

    if data_type == 1:
        while True:
            try:
                data = list(map(int, input("Введите элементы списка через пробел: ").split()))
                break
            except ValueError:
                print("Ошибка! Введите целые числа через пробел.")
        result = process_input(data)
        print(result)
    elif data_type == 2:
        while True:
            try:
                data = set(map(int, input("Введите элементы множества через пробел: ").split()))
                break
            except ValueError:
                print("Ошибка! Введите целые числа через пробел.")
        result = process_input(data)
        print(result)
    elif data_type == 3:
        while True:
            try:
                data = int(input("Введите число: "))
                break
            except ValueError:
                print("Ошибка! Введите целые число.")
        result = process_input(data)
        print(result)
    elif data_type == 4:
        data = input("Введите строку: ")
        result = process_input(data)
        print(result)
    elif data_type == 5:
        print("Работа завершена. До свидания!")
        exit()
    else:
        print("Неверный тип данных")
