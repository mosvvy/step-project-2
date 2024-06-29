from django.test import TestCase

# Create your tests here.


api_responses = [
    {
        'city': 'Lviv',
        'response': {'coord': {'lon': 24.0232, 'lat': 49.8383},
                     'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}],
                     'base': 'stations',
                     'main': {'temp': 23.87, 'feels_like': 23.77, 'temp_min': 23.87, 'temp_max': 23.87,
                              'pressure': 1011,
                              'humidity': 56, 'sea_level': 1011, 'grnd_level': 976}, 'visibility': 10000,
                     'wind': {'speed': 4.57, 'deg': 228, 'gust': 7.83}, 'clouds': {'all': 75}, 'dt': 1717245061,
                     'sys': {'country': 'UA', 'sunrise': 1717208430, 'sunset': 1717266205}, 'timezone': 10800,
                     'id': 702550,
                     'name': 'Lviv', 'cod': 200},
        'expected_result': {'weather': 'broken clouds', 'temp': 23.87, 'hum': 56, 'wind': 4.57, 'main': 'Clouds'}
    },
    {
        'city': 'Kyiv',
        'response': {'coord': {'lon': 30.5167, 'lat': 50.4333},
                     'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}],
                     'base': 'stations',
                     'main': {'temp': 27.67, 'feels_like': 30.77, 'temp_min': 27.56, 'temp_max': 29.25, 'pressure': 985,
                              'humidity': 76}, 'visibility': 10000, 'wind': {'speed': 3.84, 'deg': 154, 'gust': 5.04},
                     'clouds': {'all': 13}, 'dt': 1717255154,
                     'sys': {'type': 2, 'id': 2013236, 'country': 'UA', 'sunrise': 1717206703, 'sunset': 1717264814},
                     'timezone': 10800, 'id': 703448, 'name': 'Kyiv', 'cod': 200},
        'expected_result': {'weather': 'few clouds', 'temp': 27.67, 'hum': 76, 'wind': 3.84, 'main': 'Clouds'}
    },
    {
        'city': 'Kharkiv',
        'response': {'coord': {'lon': 36.25, 'lat': 50},
                     'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}],
                     'base': 'stations',
                     'main': {'temp': 23.54, 'feels_like': 23.28, 'temp_min': 23.54, 'temp_max': 23.54,
                              'pressure': 1017, 'humidity': 51, 'sea_level': 1017, 'grnd_level': 999},
                     'visibility': 10000, 'wind': {'speed': 2.78, 'deg': 301, 'gust': 5.31}, 'clouds': {'all': 100},
                     'dt': 1717254967, 'sys': {'country': 'UA', 'sunrise': 1717205451, 'sunset': 1717263314},
                     'timezone': 10800, 'id': 706483, 'name': 'Kharkiv', 'cod': 200},
        'expected_result': {'weather': 'overcast clouds', 'temp': 23.54, 'hum': 51, 'wind': 2.78, 'main': 'Clouds'}
    },
    {
        'city': 'London',
        'response': {'coord': {'lon': -0.1257, 'lat': 51.5085},
                     'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}],
                     'base': 'stations',
                     'main': {'temp': 16.05, 'feels_like': 15.49, 'temp_min': 14.44, 'temp_max': 17.65,
                              'pressure': 1025, 'humidity': 68}, 'visibility': 10000,
                     'wind': {'speed': 5.14, 'deg': 350}, 'clouds': {'all': 75}, 'dt': 1717254689,
                     'sys': {'type': 2, 'id': 268730, 'country': 'GB', 'sunrise': 1717213733, 'sunset': 1717272494},
                     'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200},
        'expected_result': {'weather': 'broken clouds', 'temp': 16.05, 'hum': 68, 'wind': 5.14, 'main': 'Clouds'}
    },
]


class Tests(TestCase):
    def test(self):
        assert True
