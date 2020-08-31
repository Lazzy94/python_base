# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
day_in_month_by_month_number = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

while True:
    user_input = input('Введите номер месяца: ')
    if user_input.isdigit():
        user_input = int(user_input)
        # TODO давайте тут просто проверим вхождение user_input оператором in day_in_month_by_month_number
        if day_in_month_by_month_number.get(user_input, False):
            print(f'В заданном месяце количество дней = {day_in_month_by_month_number[user_input]}')
            break
        else:
            print('Номер месяца должен быть от 1 до 12')
    else:
        print('Номер месяца должен быть числом')

# Начиная с третьего модуля буду обращать внимание на то что подчеркивает Пайчар. Придерживаемся PEP8
# Можно привести все к нужному формату code\Reformat code
