import requests
import fake_useragent
from bs4 import BeautifulSoup
import time
import json

from src.classes import SuperJobAPI, JSONSaver

# , Vacancy, HeadHunterAPI


# Создание экземпляра класса для работы с API сайтов с вакансиями
# hh_api = HeadHunterAPI()
keyword = "Python"
superjob_api = SuperJobAPI(keyword)

# Получение вакансий с разных платформ
# hh_vacancies = hh_api.get_vacancies("Python")
superjob_vacancies = superjob_api.get_request()
sj = superjob_api.get_formatted_vacancies()

# superjob_api.to_json()

# print(sj)
# with open("vacancies.json", "w", encoding="utf-8") as f:
#     json.dump(sj, f, indent=2, ensure_ascii=False)
# print(json.dumps(sj, indent=2, ensure_ascii=False))

JSONSaver(keyword).to_json()


# superjob_api.to_json(sj)

# Создание экземпляра класса для работы с вакансиями
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

# # Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
# json_saver.delete_vacancy(vacancy)

# # Функция для взаимодействия с пользователем
# def user_interaction():
#     platforms = ["HeadHunter", "SuperJob"]
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)

#     if not filtered_vacancies:
#         print("Нет вакансий, соответствующих заданным критериям.")
#         return

#     sorted_vacancies = sort_vacancies(filtered_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)


# if __name__ == "__main__":
#     user_interaction()
