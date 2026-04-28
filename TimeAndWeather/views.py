from django.shortcuts import render, redirect
from django.conf import settings
import requests
from .models import City
from datetime import datetime, timedelta, timezone


def index(request):
    api_key = settings.OPENWEATHER_API_KEY

    url = f'http://api.openweathermap.org/data/2.5/weather?q={{}}&units=metric&appid={api_key}&lang=ru'

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        try:
            response = requests.get(url.format(city)).json()

            utc_time = datetime.now(timezone.utc)
            local_time = utc_time + timedelta(seconds=response['timezone'])

            weather = {
                'id': city.id,
                'city': response['name'],
                'temperature': response['main']['temp'],
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'offset': response['timezone']
            }

            weather_data.append(weather)
        except Exception as e:
            print(f"Ошибка {city}: {e}")
            pass

    context = {'weather_data': weather_data}
    return render(request, 'index.html', context)
