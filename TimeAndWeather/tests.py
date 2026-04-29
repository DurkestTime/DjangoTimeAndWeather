from django.test import TestCase, Client
from unittest.mock import patch
from .models import City

class WeatherViewTests(TestCase):
    def setUp(self):
        city_names = ["Москва", "Moscow"]
        for name in city_names:
            City.objects.create(name=name)

    @patch('requests.get')
    def test_status_code(self, mock_get):
        mock_get.return_value.status_code = 500

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['weather_data']), 0)

    @patch('requests.get')
    def test_api_exception(self, mock_get):
        mock_get.side_effect = Exception("API is down")

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['weather_data']), 0)