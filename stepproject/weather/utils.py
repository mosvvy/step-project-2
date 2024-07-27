import requests


def get_weather(city:str):
    api_response = {'coord': {'lon': 24.0232, 'lat': 49.8383},
                    'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}],
                    'base': 'stations',
                    'main': {'temp': 23.87, 'feels_like': 23.77, 'temp_min': 23.87, 'temp_max': 23.87,
                             'pressure': 1011,
                             'humidity': 56, 'sea_level': 1011, 'grnd_level': 976}, 'visibility': 10000,
                    'wind': {'speed': 4.57, 'deg': 228, 'gust': 7.83}, 'clouds': {'all': 75}, 'dt': 1717245061,
                    'sys': {'country': 'UA', 'sunrise': 1717208430, 'sunset': 1717266205}, 'timezone': 10800,
                    'id': 702550,
                    'name': 'Lviv', 'cod': 200}

    API_KEY = "bb162c28be60f5bf4afb31a045255ad2"

    url_pattern = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    URL = url_pattern.format(city=city, api_key=API_KEY)
    response = requests.get(URL)
    api_response = response.json()

    weather = {
        'location': api_response.get('name'),
        'weather': api_response.get('weather')[0].get('main'),
        'description': api_response.get('weather')[0].get('description'),
        'temp': api_response.get('main').get('temp'),
        'temp_feels_like': api_response.get('main').get('feels_like'),
        'wind_speed': api_response.get('wind').get('speed'),
        'clouds': api_response.get('clouds').get('all'),
        'humidity': api_response.get('main').get('humidity'),
        'rain': api_response.get('rain'),
        'snow': api_response.get('snow'),
    }

    return weather