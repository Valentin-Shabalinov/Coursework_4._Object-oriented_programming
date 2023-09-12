from abc import ABC, abstractmethod
from src.exceptions import ParsingError
# from src.utils import get_currencies
import requests
import json


def get_currencies():
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    return "123455"
