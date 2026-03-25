import requests

class WeatherAppError(Exception):

    pass

def get_nsw_cities():
    pass


def get_city_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    res = requests.get(url).json()

    if "results" not in res:
        raise WeatherAppError('City not found')

    result = res["results"][0]
        return {
        "name": result["name"],
        "latitude": result["latitude"],
        "longitude": result["longitude"],
    }

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    res = requests.get(url).json()

    return res["current_weather"]