import requests
import re
import csv
from pathlib import Path

# Makes sure that extra files are read from same folder as main
BASE_DIR = Path(__file__).parent

WEATHER_FILE = BASE_DIR / "weatherCodes.csv"



class Weather:
     def __init__(self, temp, humid, wind, city, code):
          self.temp = temp
          self.humid = humid
          self.wind = wind
          self.city = city
          self.code = code


def main():
    city = welcome()
    city_cords = get_cords(city)
    weather = get_weather(city_cords[0], city_cords[1], city)
    display_weather(weather)
    



def welcome(): # Startscreen for this program
    print(f"Welcome To This Weather App")
    valid_city = False
    user_in = input(f"Please enter a city: ").strip()
    while valid_city == False:
        if re.fullmatch(r"^[A-Za-zÀ-ÖØ-öø-ÿ.' -]+$",user_in):
            valid_city = True
            return user_in
        else:
            valid_city = False
                
    
def get_cords(city): # Gets koordinates for city using API

    parameters = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    cords_url = "https://geocoding-api.open-meteo.com/v1/search"
    response = requests.get(cords_url, params=parameters)
    data = response.json()

    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]
    return latitude, longitude

def get_weather(latitude, longitude, city): # Gets weather info from API
    parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "precipitation",
            "weather_code",
            "wind_speed_10m"
        ]
    }
    weather_url = "https://api.open-meteo.com/v1/forecast"
    response = requests.get(weather_url, params=parameters)
    data = response.json()

    temp = data["current"]["temperature_2m"]
    humidity = data["current"]["relative_humidity_2m"]
    wind_speed = data["current"]["wind_speed_10m"]
    code = data["current"]["weather_code"]

    return Weather(temp, humidity, wind_speed, city, code) # Creates a weather object


def display_weather(weather): # Prints the saved weather information
        temperature = weather.temp
        humidity = weather.humid
        wind_speed = weather.wind
        city = weather.city
        condition = codeToComment(weather)
        print("\n")
        print(f"Weather information for {city}:")
        print(f"Temperature is: {temperature} C")
        print(f"Condition is {condition}")
        print(f"Humidity: {humidity} %")
        print(f"Wind speed: {wind_speed} km/h")

def ask_exit(): # Asks if user wants to exit
    if input("Do you want to exit (y/n)?") == "y":
        return True
    else:
        return False

def codeToComment(weather):
        code = weather.code
        with open(WEATHER_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row["Code"]) == code:
                    return row["Description"]
             
        return "Unknown Condition"


if __name__ == "__main__": # Only runs main function if the file is the primary code file. 
    main()