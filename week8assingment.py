import requests
import datetime

# Function to fetch current weather data
def get_current_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city + ",KE",  # Filter for Kenya cities
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"\nCurrent Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("City not found or error fetching data.")

# Function to fetch 5-day weather forecast
def get_weather_forecast(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city + ",KE",
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"\n5-Day Weather Forecast for {city}:")
        for item in data['list']:
            dt = datetime.datetime.fromtimestamp(item['dt'])
            if dt.hour == 12:  # Print forecast for noon only (example)
                print(f"\nDate: {dt.strftime('%Y-%m-%d')}")
                print(f"Temperature: {item['main']['temp']}°C")
                print(f"Condition: {item['weather'][0]['description'].capitalize()}")
    else:
        print("Error fetching forecast data.")

# Main code
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    city = input("Enter the city in Kenya: ").capitalize()
    get_current_weather(api_key, city)
    get_weather_forecast(api_key, city)
