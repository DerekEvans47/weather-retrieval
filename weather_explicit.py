import requests

def get_location():

    state = input("Please enter a state: ")
    city = input("Please enter a city: ")

    LOC_URL = f"https://api.api-ninjas.com/v1/geocoding?city={city}&state={state}&country=US"
    LOC_API_KEY = "sEKaswNq38zCb50QhLyo2g==dDZQt0Ewd6UaHHEL"

    response = requests.get(LOC_URL, headers={'X-Api-Key': LOC_API_KEY})
    if response.status_code == requests.codes.ok:
        results = response.json()[0]
        lat = results['latitude']
        long = results['longitude']
        return lat, long, city
    else:
        print("Error:", response.status_code, response.text)

def get_weather():

    lat, long, city = get_location()

    WEATHER_API_KEY = "0f46b3b007f1a796e0364ef7066aaa89"
    WEATHER_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={WEATHER_API_KEY}&units=imperial"
    
    response = requests.get(WEATHER_URL)
    if response.status_code == requests.codes.ok:
        results = response.json()
        coverage = results['weather'][0]['description']
        temp = results['main']['temp']
    else:
        print("Error:", response.status_code, response.text)

    print(f"Currently in {city} there are {coverage} and it is {temp}° Farenheit.")   

get_weather()