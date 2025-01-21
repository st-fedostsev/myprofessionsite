"""
URL configuration for projectmanagersite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main_page.views import index_page, about_page, statistic_page, relevancy_page, geography_page, skills_page, last_vacancies_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name = 'home'),
    path('about/', about_page, name = 'about'),
    path('statistic/', statistic_page, name = 'statistic'),
    path('relevance/', relevancy_page, name = 'relevance'),
    path('geography/', geography_page, name = 'geography'),
    path('skills/', skills_page, name = 'skills'),
    path('last_vacancies/', last_vacancies_page, name = 'last_vacancies'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

