from parser import xml_parser
from api import api_response
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

url = 'https://www.cbr.ru/scripts/XML_daily.asp'
s = api_response.get_response(url)
data_dict = xml_parser.xml_to_dict(s)
data_list = currency_rate.get_list_all_currency(data_dict)


def asker_for_changing_cash(list_):
    while True:
        answer_ = input('Хотите обменять валюту? (да\нет): ')
        if answer_.strip().lower() == 'нет':
            break
        elif answer_.strip().lower() == 'да':
            currency_name_ = 'Доллар США'
            cash = input(f'Сколько рублей Вам нужно обменять на {currency_name_}: ')
            calculator.parse_and_calculate_cash(currency_name_, cash, list_)
            break
        else:
            print('выходом из цикла может быть только ответы: да и нет')


currency_rate.print_all_currency_info(data_collection.data_list)
asker_for_changing_cash(data_collection.data_list)
