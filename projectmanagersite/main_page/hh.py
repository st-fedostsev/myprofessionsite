import requests
import re


class HeadHunterAPI:
    BASE_URL = 'https://api.hh.ru/vacancies'

    def __init__(self, search_text):
        self.search_text = search_text

    def _get_vacancies(self, date, count):
        params = {
            'text': self.search_text,
            'specialization': 1,
            'date_from': f"{date}T00:00:00",
            'date_to': f"{date}T23:00:00",
            'per_page': count,
            'page': 1,
        }
        response = requests.get(self.BASE_URL, params=params)
        return response.json().get('items', [])

    @staticmethod
    def _clean_html(raw_html):
        cleanr = re.compile('<.*?>')
        return re.sub(cleanr, '', raw_html).strip()

    @staticmethod
    def _shorten_text(text, max_length=100):
        return text[:max_length] + '...' if len(text) > max_length else text

    def fetch_vacancies(self, date, count):
        vacancies = self._get_vacancies(date, count)
        results = []

        for vacancy in vacancies:
            vacancy_url = f"{self.BASE_URL}/{vacancy['id']}"
            details = requests.get(vacancy_url).json()

            if not details.get('salary'):
                continue

            description = self._shorten_text(self._clean_html(details['description']))
            results.append({
                'name': details['name'],
                'description': description,
                'key_skills': [skill['name'] for skill in details.get('key_skills', [])],
                'employer': details['employer']['name'],
                'salary': f"{details['salary']['from']} - {details['salary']['to']} {details['salary']['currency']}",
                'area': details['area']['name'],
                'published_at': details['published_at'][:10],
                'alternate_url': details['alternate_url'],
            })

        return results