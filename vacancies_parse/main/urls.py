from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('general-statistics', views.general_statistics_view, name='general_statistics'),  # Страница Общая статистика
    path('demand', views.demand_view, name='demand'),  # Страница Востребованность
    path('geography', views.geography_view, name='geography'),  # Страница География
    path('skills', views.skills_view, name='skills'),  # Страница Навыки
    path("latest_vacancies", views.latest_vacancies, name="latest_vacancies"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)