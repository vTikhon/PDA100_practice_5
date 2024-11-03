from currency import currency_checker
from currency import currency_rate


def calculate_cash(currency_name_, quantity_cash, list_):
    if currency_checker.check_currency_name(currency_name_, list_):
        value = round(quantity_cash / currency_rate.get_currency(currency_name_, list_), 2)
        print(f'Вы получите: {value} {currency_name_}')
    else:
        print(f'Валюты: {currency_name_} к обмену нет')


def parse_and_calculate_cash(currency_name_, s: str, list_):
    cash = s
    try:
        cash = float(s)
        calculate_cash(currency_name_, cash, list_)
    except ValueError:
        print(f"{cash} не является числом")


def calculate_cash_inverse(currency_name_, quantity_cash, list_):
    if currency_checker.check_currency_name(currency_name_, list_):
        value = round(quantity_cash * currency_rate.get_currency(currency_name_, list_), 2)
        print(f'Вы получите: {value} рубля')
    else:
        print(f'Валюты: {currency_name_} к обмену нет')


def parse_and_calculate_cash_inverse(currency_name_, s: str, list_):
    cash = s
    try:
        cash = float(s)
        calculate_cash_inverse(currency_name_, cash, list_)
    except ValueError:
        print(f"{cash} не является числом")