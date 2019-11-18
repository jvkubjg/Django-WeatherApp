from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm

def home(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=52f8ff4361387d223395313e3bbeac63'

    err_msg = ''
    message = ''
    message_class = ''

    if request.method == "POST":
        form = CityForm(request.POST)

        if form.is_valid():
            existing_city = form.cleaned_data['name']
            number_of_cities =  City.objects.filter(name=existing_city).count()

            if number_of_cities == 0:
                r = requests.get(url.format(existing_city)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'The given city does not exist'
            else:
                err_msg = 'The city already exist'

        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added succesfully'
            message_class = 'is-success'

    form = CityForm()
    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    context = {
        'weather_data': weather_data,
        'form' : form,
        'message': message,
        'message_class': message_class
    }

    return render(request, 'TheWeather/weather.html', context)


def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')
