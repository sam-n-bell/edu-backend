import requests
from util.constants import NUMBERS_API_BASE


def get_math_fact(number, type_="trivia"):
    uri = f"{NUMBERS_API_BASE}/{number}/{type_}"
    try:
        return requests.get(uri)
    except Exception as e:
        return None

