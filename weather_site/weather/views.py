# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import requests

API_KEY = "ac337684d6f8cb09949a081135715daa"

def weather_view(request, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return JsonResponse({
        "city": city,
        "temperature": data.get("main", {}).get("temp"),
        "weather": data.get("weather")[0]["description"] if data.get("weather") else None
    })