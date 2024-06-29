from django.shortcuts import render
import weather.utils as utils

# Create your views here.


def home(request):
    return render(request, "main.html")


def get_weather(request, city):

    weather = utils.get_weather(city)

    return render(request, "weather-by-city.html", {'city': city, 'weather': weather})

