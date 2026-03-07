import requests
from geopy.geocoders import Nominatim
from countrystatecity_countries import get_states_of_country
from rich import print

print("""=====================
Weather App
=====================""")

def get_coordinate(city_name):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city_name)

    if location:
        return location.latitude, location.longitude
    return None, None

def celcious_to_fahrenheit(celcius):
    return celcius * 1.8 + 32

def celcious_to_kelvin(celcius):
    return celcius + 273.15

while True:
    city_input = input("\nInput city: ")

    kh_cities = get_states_of_country("KH")
    exists = any(c.name.lower() == city_input.lower() for c in kh_cities)

    if not exists:
        print("Error: City not found!")
        continue

    lat, lon = get_coordinate(city_input)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data["current_weather"]["temperature"]
        print(f"\nCity name: {city_input}")
        print(f"Cordinate: latitude={lat}, longitude={lon}")
        print("Temperature:")
        print(f"    {round(temperature, 2)} degrees celsius")
        print(f"    {round(celcious_to_fahrenheit(temperature), 2)} fahrenheit")
        print(f"    {round(celcious_to_kelvin(temperature), 2)} kelvin")
    else:
        print(f"Error: check your api!")





