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
    avaiable_sols = get_available_sols(data)
    current_sol = avaiable_sols[-1]
    return current_sol

def get_sol_data(data, sol):
    avaiable_sols = get_available_sols(data)
    if sol in avaiable_sols:
        sol_data = data[sol]
        return sol_data
    else:
        return f"{sol} not found."

def get_sol_temperature(sol_data):
    temperature = sol_data["AT"]
    average_temperature = temperature["av"]
    minimum_temperature = temperature["mn"]
    maximum_temperature = temperature["mx"]
    return average_temperature, minimum_temperature, maximum_temperature


# for testing
result = get_mars_data()
avaiable_sols = get_available_sols(result)


current_sol = get_current_sol(result)
sol_data = result[current_sol]
sol_temperature = sol_data["AT"]

temp = get_sol_temperature(sol_data)

print(temp)