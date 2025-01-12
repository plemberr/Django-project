from django.shortcuts import render, get_object_or_404
from .models import GeneralStatistics


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