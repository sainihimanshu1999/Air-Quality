import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=New Delhi&appid=4ee1e71fed9417ca29e961469d9ee039'
    city = 'New Delhi'

    if request.method == 'POST':
        form  = CityForm(request.POST or None)
        form.save()

    cities = City.objects.all()

    weather_data = []

    for city in cities:


        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temprature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

  

    context = {'weather_data' : city_weather, 'form': form }

    return render(request , 'home.html', context)



