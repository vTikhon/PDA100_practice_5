def check_currency_name(currency_name_: str, list_):
    currency_name_ = currency_name_.lower()
    currency = False
    for el in list_:
        if el['Name'].lower() == currency_name_:
            currency = True
    return currency