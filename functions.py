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
    return result