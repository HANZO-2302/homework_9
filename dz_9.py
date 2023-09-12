'''
Напишите функцию для транспонирования матрицы
'''
# def transpose_matrix(matrix):
# 	rows = len(matrix)
# 	cols = len(matrix[0])
#
# 	transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
#
# 	for i in range(rows):
# 		for j in range(cols):
# 			transposed_matrix[j][i] = matrix[i][j]
#
# 	return transposed_matrix
#
#
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# transposed = transpose_matrix(matrix)
# print(transposed)

'''=================================================================================================================
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хэшируем,
используйте его строковое представление.
'''
# def create_dict(**kwargs):
#     result = {}
#     for key, value in kwargs.items():
#         if not isinstance(key, (int, float, str, bool)):
#             key = str(key)
#         result[value] = key
#     return result
# result_dict = create_dict(param1='value1', param2='value2', param3='value3')
# print(result_dict)


'''==================================================================================================================
Банкомат
Разбейте её на отдельные операции — функции. 
Дополнительно сохраняйте все операции поступления
и снятия средств в список.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег




✔ не получается-------После каждой третей операции пополнения или снятия начисляются проценты - 3% 
'''
initial_balance = 0
transactions = []

def deposit(amount):
    global initial_balance
    initial_balance += amount
    transactions.append(f"Пополнение: +{amount} у.е.")

def withdraw(amount):
    global initial_balance
    if amount <= initial_balance:
        fee = max(30, min(amount * 0.015, 600))
        initial_balance -= amount + fee
        transactions.append(f"Снятие: -{amount} у.е. (включая комиссию {fee} у.е.)")
    else:
        print("Недостаточно средств на счете.")

def exit_bank():
    global initial_balance
    print(f"Остаток на счете: {initial_balance} у.е.")
    print("Последние операции:")
    for transaction in transactions:
        print(transaction)

def calculate_tax(amount):
    return amount * 0.1

def check_tax_limit(amount):
    if amount + initial_balance > 5000000:
        return True
    return False

def atm():
    while True:
        print(f"Остаток на счете: {initial_balance} у.е.")
        print("Выберите действие:")
        print("1. Пополнить")
        print("2. Снять")
        print("3. Выйти")
        choice = int(input("Введите номер действия: "))

        if choice == 1:
            amount = int(input("Введите сумму для пополнения (кратную 50): "))
            if amount % 50 == 0:
                if check_tax_limit(amount):
                    amount -= calculate_tax(amount)
                    print(f"Остаток на счете: {initial_balance} у.е.")
                deposit(amount)
            else:
                print("Сумма должна быть кратной 50.")
        elif choice == 2:
            amount = int(input("Введите сумму для снятия (кратную 50): "))
            if amount % 50 == 0:
                withdraw(amount)
            else:
                print("Сумма должна быть кратной 50.")
        elif choice == 3:
            exit_bank()
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

atm()

