from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "main.html")


def weather(request, city):
    return render(request, "weather-by-city.html", { 'city':city })
