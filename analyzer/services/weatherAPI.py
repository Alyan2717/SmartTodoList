import requests

class WeatherAPI:
    API_KEY = "909d57d8c4cc183e05748fdd1cb6fe54"

    @staticmethod
    def get_weather(city="Berlin"):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WeatherAPI.API_KEY}&units=metric"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return {
                "temp": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            }
        except Exception as e:
            return {"error": str(e)}