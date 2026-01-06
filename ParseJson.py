import json
import requests
from pathlib import Path

CONFIG_PATH = Path("config.json")

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

API_KEY = config.get("openweather_api_key")

CITY = "Newark"
URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
}

response = requests.get(URL, params=params)
response.raise_for_status()

data = response.json()

print(data)


print(f"City: {data['name']}")
print(f"Temperature: {data['main']['temp']} °C")
print(f"Condition: {data['weather'][0]['description']}")
print(f"Humidity: {data['main']['humidity']}%")
print(f"Wind Speed: {data['wind']['speed']} m/s")
print()