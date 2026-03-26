import requests


class WeatherAppError(Exception):
    pass


def get_nsw_cities():
    return [
        "Sydney",
        "Newcastle",
        "Wollongong",
        "Central Coast",
        "Maitland",
        "Coffs Harbour",
        "Wagga Wagga",
        "Albury",
        "Tamworth",
        "Orange",
    ]


def get_city_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response = requests.get(url)

    if response.status_code != 200:
        raise WeatherAppError("Failed to connect to geocoding service.")

    data = response.json()

    if "results" not in data or not data["results"]:
        raise WeatherAppError("City not found.")

    result = data["results"][0]
    return {
        "name": result["name"],
        "latitude": result["latitude"],
        "longitude": result["longitude"],
    }


def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)

    if response.status_code != 200:
        raise WeatherAppError("Failed to connect to weather service.")

    data = response.json()

    if "current_weather" not in data:
        raise WeatherAppError("Weather data not available.")

    return data["current_weather"]


def format_weather_output(location, weather):
    return (
        f"\nWeather for {location['name']}:\n"
        f"Temperature: {weather['temperature']}°C\n"
        f"Wind Speed: {weather['windspeed']} km/h\n"
    )
