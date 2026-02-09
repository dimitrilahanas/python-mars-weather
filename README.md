# Python-Mars-Weather

A Python project that fetches and serves Mars weather data from NASA’s InSight lander API.  
⚠️ **Note:** This project is for learning purposes. It demonstrates API handling, data modelling, and serving data via FastAPI.  

---

## 📌 About the Project

Python-Mars-Weather is a structured project to fetch, model, and expose Mars weather data.  
It demonstrates how to:

- Work with REST APIs and environment variables
- Parse nested JSON data
- Structure reusable classes and methods
- Serve data through a simple API
- Model data objects for app-friendly consumption

This project can be used as a **backend for a Mars weather dashboard** (e.g., web app or Flutter app).  

---

## ✨ Features

- Fetch Mars weather data directly from NASA’s InSight API
- List all available Martian Sols
- Retrieve the most recent Sol
- Return detailed weather data for a specific Sol:
  - Average temperature
  - Current Martian season
  - Most common wind direction
  - Average wind speed
- Exposed as a **FastAPI service** for easy consumption by other applications

---

## 🗂 Tech Stack

- **Python 3.9+**
- **FastAPI** – lightweight web API framework
- **Requests** – HTTP requests to the NASA API
- **python-dotenv** – for managing environment variables (NASA API key)

---

## 🗂 Project Structure

python-mars-weather/ <br>
├─ main.py             # FastAPI app with endpoints<br>
├─ .env                # Stores NASA API key<br>
├─ app/<br>
│   ├─ __init__.py<br>
│   ├─ mars_data.py    # MarsData class to fetch API data<br>
│   ├─ commands.py     # Commands class to process and return Sol data<br>
│   └─ models/<br>
│       ├─ __init__.py<br>
│       └─ sol.py      # Sol model<br>



---

### FastAPI Endpoints

| Endpoint         | Description                               |
|-----------------|-------------------------------------------|
| `/available`     | Returns a list of all available Sols     |
| `/{sol}`         | Returns weather data for the given Sol   |

Example `/1001` response:

```json
{
  "temperature": -65.2,
  "season": "spring",
  "wind_direction": "NW",
  "wind_speed": 5.6
}