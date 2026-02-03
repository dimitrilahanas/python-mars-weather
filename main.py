from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("NASA_API_KEY")

def get_mars_data():
    url = f"https://api.nasa.gov/insight_weather/?api_key={API_KEY}&feedtype=json&ver=1.0"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

def get_available_sols(data):
    available_sols = data["sol_keys"]
    return available_sols

def get_current_sol(data):
    available_sols = get_available_sols(data)
    current_sol = available_sols[-1]
    return current_sol

def get_sol_data(data, sol):
    available_sols = get_available_sols(data)
    if sol in available_sols:
        sol_data = data[sol]
        return sol_data
    else:
        return f"{sol} not found."

def get_sol_temperature(sol_data):
    temperature = sol_data["AT"]
    average_temperature = temperature["av"]
    return f"{average_temperature} degrees C"

def get_sol_season(sol_data):
    current_season = sol_data["Season"]
    return current_season

def get_sol_wind_direction(sol_data):
    wind = sol_data["WD"]
    wind_direction = wind["most_common"]
    compass_point = wind_direction["compass_point"]
    return compass_point

def get_sol_wind_speed(sol_data):
    horizontal_speed = sol_data["HWS"]
    average_speed = horizontal_speed["av"]

    return f"{average_speed} m/s"

# for testing
result = get_mars_data()
current_sol = get_current_sol(result)
sol_data = get_sol_data(result, current_sol)
season = get_sol_season(sol_data)
wind_direction = get_sol_wind_direction(sol_data)
speed = get_sol_wind_speed(sol_data)

print(speed)