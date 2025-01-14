from django.shortcuts import render, get_object_or_404
from .models import GeneralStatistics
from datetime import datetime, timedelta
import requests

def index(request):
    return render(request, 'main/index.html')


def general_statistics_view(request):
    # Получаем объект GeneralStatistics
    general_statistics = GeneralStatistics.objects.get(id=1)

    # Получаем все разделы, связанные с объектом GeneralStatistics
    sections = general_statistics.sections.all()

    # Передаем данные в шаблон
    return render(request, 'main/general_statistics.html', {
        'sections': sections
    })

def demand_view(request):
    demand = GeneralStatistics.objects.get(id=2)

    # Получаем все разделы, связанные с объектом GeneralStatistics
    sections = demand.sections.all()

    # Передаем данные в шаблон
    return render(request, 'main/demand.html', {
        'sections': sections
    })

def geography_view(request):
    geography = GeneralStatistics.objects.get(id=3)

    # Получаем все разделы, связанные с объектом GeneralStatistics
    sections = geography.sections.all()

    # Передаем данные в шаблон
    return render(request, 'main/geography.html', {
        'sections': sections
    })

def skills_view(request):
    skills = GeneralStatistics.objects.get(id=4)

    # Получаем все разделы, связанные с объектом GeneralStatistics
    sections = skills.sections.all()

    # Передаем данные в шаблон
    return render(request, 'main/skills.html', {
        'sections': sections
    })

# Страница Последние вакансии

def get_java_vacancies():
    date_to = datetime.now()
    date_from = date_to - timedelta(days=1)

    url = "https://api.hh.ru/vacancies"
    params = {
        "text": "java OR джава OR ява",
        "date_from": date_from.strftime("%Y-%m-%dT%H:%M:%S"),
        "date_to": date_to.strftime("%Y-%m-%dT%H:%M:%S"),
        "per_page": 10,
        "page": 0,
    }

    headers = {"User-Agent": "JavaVacancyFetcher/1.0"}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        vacancies = response.json().get("items", [])
        detailed_vacancies = []

        for vacancy in vacancies:
            if not contains_keywords(vacancy["name"], ["java", "джава", "ява"]):
                continue

            vacancy_id = vacancy["id"]
            vacancy_details = requests.get(f"{url}/{vacancy_id}", headers=headers).json()

            detailed_vacancies.append({
                "name": vacancy_details.get("name"),
                "description": vacancy_details.get("description", None),
                "skills": ", ".join(skill["name"] for skill in vacancy_details.get("key_skills", [])),
                "company": vacancy_details.get("employer", {}).get("name", None),
                "salary": format_salary(vacancy_details.get("salary")),
                "region": vacancy_details.get("area", {}).get("name", None),
                "published_at": format_date(vacancy_details.get("published_at")),
            })

        return detailed_vacancies
    else:
        return None

def contains_keywords(text, keywords):
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in keywords)

def format_salary(salary):
    if not salary:
        return None
    if salary["from"] and salary["to"]:
        return f"{salary['from']} - {salary['to']} {salary['currency']}"
    elif salary["from"]:
        return f"От {salary['from']} {salary['currency']}"
    elif salary["to"]:
        return f"До {salary['to']} {salary['currency']}"
    return None

def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")
        return date_obj.strftime("%d.%m.%Y, %H:%M")
    except ValueError:
        return None

def latest_vacancies(request):
    vacancies = get_java_vacancies()
    return render(request, "main/latest_vacancies.html", {"vacancies": vacancies})
