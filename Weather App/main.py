import requests


def main():

    print(get_cords(input("Enter City: ")))



def get_cords(city):

    parameters = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get("https://geocoding-api.open-meteo.com/v1/search", params=parameters)
    data = response.json()

    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]
    return latitude, longitude

if __name__ == "__main__": # Only runs main function if the file is the primary code file. 
    main()