from functions import (
    WeatherAppError,
    format_weather_output,
    get_city_coordinates,
    get_nsw_cities,
    get_weather,
)


def show_menu() -> None:
    print("\n=== NSW Weather App ===")
    print("1. List NSW cities")
    print("2. Get weather for a city")
    print("3. Exit")


def prompt_choice() -> str:
    return input("Choose an option (1-3): ").strip()


def list_cities() -> None:
    cities = get_nsw_cities()
    print("\nNSW cities:")
    for idx, city in enumerate(cities, start=1):
        print(f"{idx}. {city}")


def weather_for_city() -> None:
    city = input("Enter city name: ").strip()
    if not city:
        print("City name is required.")
        return

    try:
        location = get_city_coordinates(city)
        weather = get_weather(location["latitude"], location["longitude"])
        print(format_weather_output(location, weather))
    except WeatherAppError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def main() -> None:
    while True:
        show_menu()
        choice = prompt_choice()

        if choice == "1":
            list_cities()
        elif choice == "2":
            weather_for_city()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    main()