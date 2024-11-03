from parser import xml_parser
from api import api_response
from currency import currency_rate
from data import url


url = url.url
s = api_response.get_response(url)
data_dict = xml_parser.xml_to_dict(s)
data_list = currency_rate.get_list_all_currency(data_dict)