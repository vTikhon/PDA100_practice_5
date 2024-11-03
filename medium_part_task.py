from currency import currency_rate
from currency import calculator
from data import data_collection

# Написать программу «Обмен валюты»
# Обязательное задание:
# • Отправить запрос к API ЦБ РФ(https://www.cbr.ru/scripts/XML_daily.asp)
# и получить информацию о курсах валют на сегодняшний день
# • Предложить пользователю обменять рубли на доллары
# • Пользователь вводит число(сумму, которую собирается обменять)
# • Ответом программы должна быть конвертированная сумма в доллары
# • Желательно, хранить функции в разных модулях (модуль для работы с api и пр.)
# Пример:
# Сколько рублей Вам нужно обменять: 10000
# Вы получите: 106.93 доллара

# Задание средней сложности:
# • На первом шаге предложить пользователю выбор, что он меняет
# «рубли/доллары»
# • Если меняет рубли на доллары, то ответ как в базовом задании
# • Если меняет доллары на рубли, то ответ в рублях
# • Предусмотреть проверки


def asker_for_changing_cash(list_):
    flag = True
    while flag:
        answer_ = input('Хотите обменять валюту? (да\нет): ')
        if answer_.strip().lower() == 'нет':
            break
        elif answer_.strip().lower() == 'да':
            while flag:
                currency_name_ = 'Доллар США'
                variant_ = input(f'Вы хотите поменять: 1. рубли на {currency_name_} или 2. {currency_name_} на рубли ? 0. выход из вопроса: ')
                if variant_.strip() == '0':
                    print('Выхожу из вопроса')
                    flag = False
                elif variant_.strip() == '1':
                    cash = input(f'Сколько рублей Вам нужно обменять на {currency_name_}: ')
                    calculator.parse_and_calculate_cash(currency_name_, cash, list_)
                    flag = False
                elif variant_.strip() == '2':
                    cash = input(f'Сколько {currency_name_} Вам нужно обменять на рубли: ')
                    calculator.parse_and_calculate_cash_inverse(currency_name_, cash, list_)
                    flag = False
                else:
                    print('должны выбрать варианты: 1, 2, или 0')
        else:
            print('выходом из цикла может быть только ответы: да и нет')


currency_rate.print_all_currency_info(data_collection.data_list)
asker_for_changing_cash(data_collection.data_list)
