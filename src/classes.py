from abc import ABC, abstractmethod
from src.exceptions import ParsingError

import requests
import json

import math


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass


class HeadHunterAPI(Engine):
    url = "https://api.hh.ru/vacancies"

    def __init__(self, keyword) -> None:
        self.keyword = keyword

        self.headers = {"User-Agent": "Your User Agent"}

        self.vacancies = []

    def get_request(self):
        self.params = {
            "text": self.keyword,
            "page": None,
            "archived": False,
            "per_page": 10,
        }

        response = requests.get(self.url, params=self.params, headers=self.headers)
        if response.status_code != 200:
            raise ParsingError(
                f"Ошибка получения ваккансий! Статус: {response.status_code}"
            )
        return response.json()

    def get_formatted_vacancies(self):
        self.formatted_vacancies = []

        for vacancy in self.get_request()["items"]:
            formatted_vacancy = {
                "employer": vacancy["employer"]["name"],
                "title": vacancy["name"],
                "url": vacancy["employer"]["alternate_url"],
                "api": "HeadHunter",
                "salary_from": vacancy["salary"]["from"]
                if vacancy["salary"] and vacancy["salary"]["from"] != 0
                else None,
                "salary_to": vacancy["salary"]["to"]
                if vacancy["salary"] and vacancy["salary"]["to"] != 0
                else None,
            }

            self.formatted_vacancies.append(formatted_vacancy)

        return self.formatted_vacancies


class SuperJobAPI(Engine):
    url = "https://api.superjob.ru/2.0/vacancies/"

    def __init__(self, keyword):
        self.keyword = keyword
        self.headers = {
            "X-Api-App-Id": "v3.r.137812635.0c8a16f792411dc1efeff70c14d30563356b6d6e.2999f28ec7609e85a5fca040856f126b814613f3",
        }

        self.vacancies = []

    def get_request(self):
        self.params = {
            "keyword": self.keyword,
            "page": None,
            "not_archive": True,
            "count": 10,
        }

        response = requests.get(self.url, params=self.params, headers=self.headers)
        if response.status_code != 200:
            raise ParsingError(
                f"Ошибка получения ваккансий! Статус: {response.status_code}"
            )

        return response.json()["objects"]

    def get_formatted_vacancies(self):
        self.formatted_vacancies = []

        for vacancy in self.get_request():
            formatted_vacancy = {
                "employer": vacancy["firm_name"],
                "title": vacancy["profession"],
                "url": vacancy["link"],
                "api": "SuperJob",
                "salary_from": vacancy["payment_from"]
                if vacancy["payment_from"] and vacancy["payment_from"] != 0
                else None,
                "salary_to": vacancy["payment_to"]
                if vacancy["payment_to"] and vacancy["payment_to"] != 0
                else None,
            }

            self.formatted_vacancies.append(formatted_vacancy)

        return self.formatted_vacancies


class JSONSaver:
    def __init__(self, keyword):
        self.a = HeadHunterAPI(keyword)
        self.b = SuperJobAPI(keyword)

    def to_json(self):
        hh = self.a.get_formatted_vacancies()
        sj = self.b.get_formatted_vacancies()

        hh.extend(sj)

        with open("vacancies.json", "w", encoding="utf-8") as file:
            json.dump(hh, file, indent=2, ensure_ascii=False)

    def add_vacancy():
        pass

    def get_vacancies_by_salary(self):
        with open("vacancies.json") as json_file:
            data = json.load(json_file)
            newlist = sorted(
                data,
                key=lambda d: math.inf
                if d["salary_from"] == None
                else d["salary_from"],
            )

        return newlist

    def get_vacancies_by_salary_reverse(self):
        with open("vacancies.json") as json_file:
            data = json.load(json_file)
            newlist = sorted(
                data,
                key=lambda d: 0 if d["salary_from"] == None else d["salary_from"],
                reverse=False,
            )

        return newlist
