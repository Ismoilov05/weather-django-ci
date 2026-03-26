from django.test import TestCase
from django.urls import reverse

class WeatherTestCase(TestCase):

    def test_weather_endpoint(self):
        response = self.client.get('/weather/Tashkent/')
        self.assertEqual(response.status_code, 200)