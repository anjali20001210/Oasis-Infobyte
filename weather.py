import requests

# API key from OpenWeatherMap (replace 'your_api_key' with your actual API key)
API_KEY = "your_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(location):
    try:
        # Send request to the API
        response = requests.get(f"{BASE_URL}?q={location}&appid={API_KEY}&units=metric")
        # Raise an exception if the request failed
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error occurred: {err}")
    return None

def display_weather_info(weather_data):
    if weather_data:
        # Extract relevant data
        city = weather_data['name']
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_description = weather_data['weather'][0]['description']

        # Display the weather information
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description.capitalize()}")
    else:
        print("Failed to retrieve weather data.")

def main():
    print("Welcome to the Basic Weather App!")

    # Get user input for location
    location = input("Enter city name or ZIP code: ")

    # Fetch weather data
    weather_data = get_weather_data(location)

    # Display the weather info
    display_weather_info(weather_data)

if __name__ == "__main__":
    main()
