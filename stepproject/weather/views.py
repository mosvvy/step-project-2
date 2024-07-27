from django.shortcuts import render
import weather.utils as utils
from weather.models import SearchHistory

# Create your views here.


def home(request):
    return render(request, "main.html")


def get_weather(request, city):

    if request.user:
        weather = utils.get_weather(city)
        search_result = SearchHistory(user=request.user, city=city, result=weather)
        search_result.save()

    return render(request, "weather-by-city.html", {'city': city, 'weather': weather})


def get_history(request):
    history = SearchHistory.objects.filter(user=request.user)
    print(history)
    return render(request, "list.html", {'list': history})

