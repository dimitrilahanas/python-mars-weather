from dotenv import load_dotenv
import os
import requests

class MarsData:
    load_dotenv(dotenv_path=".env")
    API_KEY = os.getenv("NASA_API_KEY")

    @staticmethod
    def get_mars_data():
        url = f"https://api.nasa.gov/insight_weather/?api_key={MarsData.API_KEY}&feedtype=json&ver=1.0"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"