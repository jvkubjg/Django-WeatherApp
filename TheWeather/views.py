from django.shortcuts import render
import requests
# Create your views here.

def home(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=52f8ff4361387d223395313e3bbeac63'
    city = 'Las Vegas'

    r = requests.get(url.format(city))
    print(r.text)
    return render(request, 'TheWeather/weather.html')
