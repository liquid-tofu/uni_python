from geopy.geocoders import Nominatim
from countrystatecity_countries import get_states_of_country
from rich import print
from utility import Area59

print("""=====================
Weather App
=====================""")

def get_coordinate(city_name):
    geolocator = Nominatim(user_agent="meow_app")
    location = geolocator.geocode(city_name)

    if location:
        return location.latitude, location.longitude
    return None, None

while True:
    city_input = input("\nInput city: ")
    kh_cities = get_states_of_country("KH")
    exists = any(c.name.lower() == city_input.lower() for c in kh_cities)

    if not exists:
        print("Error: City not found!")
        continue

    x, y = get_coordinate(city_input)
    weather = Area59(city_input, x, y)

    if weather.get_status() == 200:
        print(f"\nCity name: {city_input}")
        print(f"Cordinate: latitude={x}, longitude={y}")
        print("Temperature:")
        print(f"    {round(weather.get_celcius(), 2)} degrees celsius")
        print(f"    {round(weather.get_fahrenheit(), 2)} fahrenheit")
        print(f"    {round(weather.get_kelvin(), 2)} kelvin")
    else:
        print(f"Error: check your api!")





