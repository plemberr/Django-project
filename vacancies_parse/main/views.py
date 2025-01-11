from django.shortcuts import render, get_object_or_404
from .models import GeneralStatistics


def index(request):
    return render(request, 'main/index.html')


def general_statistics_view(request):
    # Получаем объект GeneralStatistics, например, с id=1
    general_statistics = GeneralStatistics.objects.get(id=1)

    # Получаем первый раздел (если он существует)
    first_section = general_statistics.sections.first()

    # Передаем данные в шаблон
    return render(request, 'main/general_statistics.html', {
        'first_section': first_section
    })
