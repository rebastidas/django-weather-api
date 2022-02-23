from unicodedata import name
from django.urls import path
from .views import WeatherInfo

urlpatterns =[
    path('weather-info',WeatherInfo.as_view()),
    ]