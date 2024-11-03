from currency import currency_checker

def get_list_all_currency(dict_: dict):
    return dict_['ValCurs']['Valute']

def get_currency(currency_name_: str, list_):
    currency_name_ = currency_name_.lower()
    currency = None
    if currency_checker.check_currency_name(currency_name_, list_):
        for el in list_:
            if el['Name'].lower() == currency_name_:
                try:
                    currency = float(el['Value'].replace(',', '.'))
                except ValueError:
                    print(f"Ошибка при преобразовании курса валюты: {el['Value']}")
                break
    return currency


def print_all_currency_info(list_):
    for el in list_:
        print(f"{el['Name']}: {el['VunitRate']}")
    print('\n')