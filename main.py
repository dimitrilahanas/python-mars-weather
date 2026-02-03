import requests

def get_mars_data():
    url = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"
    response = requests.get(url)

    match response.status_code:
        case 200:
            data = response.json()
            return data
        case 201:
            return "New resource created."
        case 204:
            return "Succeful but no data returned."
        case 400:
            return "Invalid request."
        case 401:
            return "Missing API key."
        case 500:
            return "Server error."
        
result = get_mars_data()
print(result)