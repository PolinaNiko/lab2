def is_natural_number(value):
    try:
        num = int(value)
        return num > 0
    except ValueError:
        return False

def is_number(value):
    try:
        num = int(value)
        return num
    except ValueError:
        return False

def input_natural_number(prompt):
    while True:
        user_input = input(prompt)
        if is_natural_number(user_input):
            return int(user_input)
        else:
            print("Введите натуральное число.")

def input_number(prompt):
    while True:
        user_input = input(prompt)
        if is_number(user_input):
            return int(user_input)
        else:
            print("Введите число. ")

n = input_natural_number("Введите размерность квадратной матрицы: ")

matrix = []

for i in range(n):
    row = []
    for j in range(n):
        element = input_number(f"Введите элемент [{i+1}][{j+1}]: ")
        row.append(element)
    matrix.append(row)

column_sums = [0] * n

for j in range(n):
    has_negative = False
    for i in range(n):
        if matrix[i][j] < 0:
            has_negative = True
            break
        column_sums[j] += matrix[i][j]
    if has_negative:
        column_sums[j] = 0
        print(f"В столбце {j + 1} есть отрицательные элементы.")
    else:
        print(f"Сумма элементов в столбце {j + 1}: {column_sums[j]}")