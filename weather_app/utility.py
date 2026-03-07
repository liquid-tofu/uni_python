import requests

class Area59:
    def __init__(self, city_name, lat, lon):
        self.city_name = city_name
        self.lat = lat
        self.lon = lon
        self.response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")

    def get_status(self):
        return self.response.status_code

    def get_celcius(self):
        return self.response.json()["current_weather"]["temperature"]

    def get_fahrenheit(self):
        return self.get_celcius() * 1.8 + 32

    def get_kelvin(self):
        return self.get_celcius() + 273.15

