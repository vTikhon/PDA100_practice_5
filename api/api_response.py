import requests


def get_response(url_):
    return requests.get(url_).text


