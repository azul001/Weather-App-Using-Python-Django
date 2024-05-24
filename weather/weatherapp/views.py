from django.shortcuts import render
import requests
import datetime


def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'indore'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7328e9206cb8aa6cfbe1e4d34fb48698'
    params = {'units': 'metric'}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
    else:
        description = "Weather data not available"
        icon = ""
        temp = ""

    day = datetime.date.today()

    return render(request, 'index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day,'city':city})
