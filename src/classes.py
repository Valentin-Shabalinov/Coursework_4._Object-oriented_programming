from abc import ABC, abstractmethod
from src.exceptions import ParsingError
from src.utils import get_currencies
import requests
import json


class Engine(ABC):

    @abstractmethod
    def get_request(self):
        pass

    # @abstractmethod
    # def get_vacancies(self):
    #     pass


# class HeadHunterAPI(Engine):
#     url = "https://api.hh.ru/vacancies"

#     def __init__(self, keyword) -> None:
#         self.params = {
#             "text": keyword,
#             "page": None,
#             "archived": False,
#             "per_page": 100,
#         }

#         self.headers = {"User-Agent": "Your User Agent"}

#         self.vacancies = []


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
            "count": 4,
        }

        response = requests.get(self.url, params=self.params, headers=self.headers)
        if response.status_code != 200:
            raise ParsingError(f"Ошибка получения ваккансий! Статус: {response.status_code}")

        return response.json()["objects"]

    def get_formatted_vacancies(self):
        self.formatted_vacancies = []

        for vacancy in self.get_request():
            formatted_vacancy = {
                "employer": vacancy["firm_name"],
                "title": vacancy["profession"],
                "url": vacancy["link"],
                "api": "SuperJob",
                "salary_from": vacancy["payment_from"] if vacancy["payment_from"] and vacancy["payment_from"] != 0 else None,
                "salary_to": vacancy["payment_to"] if vacancy["payment_to"] and vacancy["payment_to"] != 0 else None,
            }

            self.formatted_vacancies.append(formatted_vacancy)

        return self.formatted_vacancies


    # def get_vacancies(self, pages_count=2):
    #     self.vacancies = []
    #     for page in range(pages_count):
    #         page_vacancies = []
    #         self.params["page"] = page
    #         print(f"({self.__class__.__name__}) Парсинг страницы {page} -", end=" ") 
    #         try:
    #             page_vacancies = self.get_request()
    #         except ParsingError as error:
    #             print(error)
    #         else:
    #             self.vacancies.extend(page_vacancies)
    #             print(f"Загружено вакансий: {len(page_vacancies)}")

    #         if len(page_vacancies) == 0:
    #             break



class JSONSaver(SuperJobAPI):
    
    def __init__(self, keyword):
        super().__init__(keyword)


    def to_json(self):
        ddd = super().get_formatted_vacancies()
        with open("vacancies.json", "w", encoding="utf-8") as f:
            json.dump(ddd, f, indent=2, ensure_ascii=False)



# class Vacancy:
#     def __init__(self, vacancy) -> None:
#         pass