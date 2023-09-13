import json

from src.classes import SuperJobAPI, HeadHunterAPI, JSONSaver


keyword = input("Введите ключевое слово для поиска вакансий: ")

sj_api = SuperJobAPI(keyword)
hh_api = HeadHunterAPI(keyword)


action = input(
    "Получить список вакансий с SuperJob: введите 1\n"
    "Получить список вакансий с HeadHunter: введите 2\n"
    "Завершить: введите exit\n>>>"
)

if action == "1":
    sj = sj_api.get_formatted_vacancies()
    print(json.dumps(sj, indent=2, ensure_ascii=False))


elif action == "2":
    hh = hh_api.get_formatted_vacancies()
    print(json.dumps(hh, indent=2, ensure_ascii=False))


elif action.lower() == "exit":
    exit()


json_s = JSONSaver(keyword)
json_s.to_json()


action = input(
    "Получить список всех вакансий по возрастанию цены ОТ: введите 1\n"
    "Получить список всех вакансий по убыванию цены ОТ: введите 2\n"
    "Завершить: введите exit\n>>>"
)

if action == "1":
    increase = json_s.get_vacancies_by_salary_reverse()
    print(json.dumps(increase, indent=2, ensure_ascii=False))


elif action == "2":
    increase = JSONSaver(keyword).get_vacancies_by_salary()
    print(json.dumps(increase, indent=2, ensure_ascii=False))

elif action.lower() == "exit":
    exit()
