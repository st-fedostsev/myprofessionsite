from django.shortcuts import render
from .models import StatisticsData

# Create your views here.
def index_page(request):
    return render(request, 'index.html', {'active_page': 'home'})

def about_page(request):
    return render(request, 'about.html', {'active_page': 'about'})

def statistic_page(request):
    statistics_data = StatisticsData.objects.all()  # Получаем все изображения
    return render(request, 'statistic.html', {'active_page': 'statistic', 'statistics_data': statistics_data})

def geography_page(request):
    return render(request, 'geography.html', {'active_page': 'geography'})

def relevancy_page(request):
    return render(request, 'relevance.html', {'active_page': 'relevance'})

def skills_page(request):
    return render(request, 'skills.html', {'active_page': 'skills'})

def last_vacancies_page(request):
    return render(request, 'last_vacancies.html', {'active_page': 'last_vacancies'})


