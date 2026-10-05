import requests


def main():
    city_cords = get_cords(welcome())
    weather_info = get_weather(city_cords[0], city_cords[1])
    display_weather(weather_info)
    



def welcome():
    print(f"Welcome To This Weather App")
    return input(f"Please enter a city: ")


def get_cords(city):

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

def get_weather(latitude, longitude):
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

    return {"Temp": temp, "humid": humidity, "wind": wind_speed}


def display_weather(weather_info):
        temperature = weather_info["Temp"]
        humidity = weather_info["humid"]
        wind_speed = weather_info["wind"]
    
        print(f"{temperature} C")
        print(f"{humidity} %")
        print(f"{wind_speed} m/s")


if __name__ == "__main__": # Only runs main function if the file is the primary code file. 
    main()