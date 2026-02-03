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

def get_avaliable_sols(data):
    avaliable_sols = data["sol_keys"]
    return avaliable_sols

def get_current_sol(data):
    avaiable_sols = get_avaliable_sols(data)
    current_sol = avaiable_sols[-1]
    return current_sol

# for testing
result = get_mars_data()
avaiable_sols = get_avaliable_sols(result)
current_sol = get_current_sol(result)
print(current_sol)