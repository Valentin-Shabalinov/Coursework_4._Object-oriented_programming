import requests
import json


class HeadHunterAPI:

    def __init__(self) -> None:
        # self.keyword = keyword
        pass



    def get_vacancies(self, keyword):
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": keyword,
            "area": 1,  # Specify the desired area ID (1 is Moscow)
            "per_page": 20,  #Number of vacancies per page 
        }
        headers = {
            "User-Agent": "Your User Agent",  # Replace with your User-Agent header
        }

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            vacancies = data.get("items", [])
            for vacancy in vacancies:
                # Extract relevant information from the vacancy object
                self.vacancy_id = vacancy.get("id")
                self.vacancy_title = vacancy.get("name")
                self.vacancy_url = vacancy.get("alternate_url")
                self.company_name = vacancy.get("employer", {}).get("name")
                self.requirement = vacancy.get("snippet", {}).get("requirement")
                # self.salary = vacancy["salary"]["from"]
                # if not self.salary:
                #     print("---------")
                # professional_roles = vacancy.get("professional_roles", {}).get("name")
                # professional_roles = vacancy["professional_roles"]["name"]
                # print(f"ID: {self.vacancy_id}\nTitle: {self.vacancy_title}\nCompany: {self.company_name}\nURL: {self.vacancy_url}\nТребования: {self.requirement}\n")
                # print(json.dumps(vacancy, indent=2, ensure_ascii=False))
                print(self.vacancy_id)
        else:
            print(f"Request failed with status code: {response.status_code}")
            # print(json.dumps(data, indent=2, ensure_ascii=False))


hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies("Python")

print(hh_vacancies)