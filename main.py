from dotenv import load_dotenv
from fastapi import FastAPI
import os
import requests

app = FastAPI()

load_dotenv()
API_KEY = os.getenv("NASA_API_KEY")

def get_mars_data():
    url = f"https://api.nasa.gov/insight_weather/?api_key={API_KEY}&feedtype=json&ver=1.0"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

@app.get("/avaliable-sols")
def get_available_sols():
    data = get_mars_data()
    return data["sol_keys"]

@app.get("/current-sol")
def get_current_sol():
    data = get_mars_data()
    return data["sol_keys"][-1]

@app.get("/sol-temp/{sol}")
def get_sol_temperature(sol: str):
    data = get_mars_data()
    sol_data = data[sol]
    temperature = sol_data["AT"]
    return f"{temperature["av"]} degrees C"

@app.get("/sol-season/{sol}")
def get_sol_season(sol: str):
    data = get_mars_data()
    sol_data = data[sol]
    return sol_data["Season"]

@app.get("/sol-wind-direction/{sol}")
def get_sol_wind_direction(sol: str):
    data = get_mars_data()
    sol_data = data[sol]
    wind = sol_data["WD"]
    wind_direction = wind["most_common"]
    return wind_direction["compass_point"]

@app.get("/sol-wind-speed/{sol}")
def get_sol_wind_speed(sol: str):
    data = get_mars_data()
    sol_data = data[sol]
    horizontal_speed = sol_data["HWS"]
    return f"{horizontal_speed["av"]} m/s"