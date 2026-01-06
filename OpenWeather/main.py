import json
import requests
from pathlib import Path


CONFIG_PATH = Path("config.json") # The API key is stored here
API_URL = "https://api.openweathermap.org/data/2.5/weather" # API endpoint

MAX_FAVOURITES = 3 # The maximum number of favorite cities allowed
favourites = [] 


with open(CONFIG_PATH, "r") as f: # Loading the config file json
    config = json.load(f)

API_KEY = config.get("openweather_api_key") # parsing the json to get the contets of the key openweather_api_key

def get_weather(city: str) -> dict: 
    params = {                          # The minimum required parameters avcording to OpenWeatherMap API documentation
        "q": city,
        "appid": API_KEY,
    }

    response = requests.get(API_URL, params=params) 

    response.raise_for_status()
    return response.json()


def print_weather(data: dict): # parsing the data and only printing relevant information about the cities
    print("\nWeather Details")
    print("----------------")
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']} °C")
    print(f"Condition: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
    print()


def main():
    while True:
        print("1. Search weather by city") # Menu options
        print("2. Add city to favourites")
        print("3. Remove city from favourites")
        print("4. List favourite cities")
        print("5. Exit")



        choice = input("Select an option: ").strip()

        if choice == "1": # Runs when the user choses option 1
            city = input("Enter city name: ").strip()
            data = get_weather(city) # calls the get_weather function and prints the data
            print_weather(data)

        elif choice == "2":
            city = input("Enter city name to add: ").strip()

            if city in favourites: # Does not allow duplicates
                print("City already in favourites\n")
                continue

            if len(favourites) >= MAX_FAVOURITES: # Does not allow more than 3 favourites
                print("Favourites list is full (max 3). Remove one first.\n")
                continue

            favourites.append(city) # If the value is valid, then it is appended
            print(f"{city} added to favourites\n")

        elif choice == "3":

            print("\nFavourite Cities:")
            for i, city in enumerate(favourites, start=1): # runs through the list and prints the cities
                print(f"{city}")

            selection = input("Select city number to remove: ").strip()

            index = int(selection) - 1 # converts the user input to an integer and adjusts for 0-based index

            removed_city = favourites.pop(index) # removes the city from list
            print(f"{removed_city} removed from favourites\n")

        elif choice == "4":
            for city in favourites: # loops through the favorit cities and prints their weather data
                data = get_weather(city)
                print_weather(data)
                

        
        elif choice == "5": # Exit menu option
            break    

        else: # Handles other inputs
            print("Invalid option\n")


if __name__ == "__main__":
    main()
