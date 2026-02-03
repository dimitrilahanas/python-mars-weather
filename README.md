# Python-Mars-Weather

A Python project that fetches and processes Mars weather data from NASA’s InSight lander API.  
⚠️ Note: This project is for learning purposes.  
I created it while learning Python, APIs, and data handling. The code is intentionally simple and focused on understanding concepts rather than being production-ready.

---

## 📌 About the Project

This project is a Python-based Mars weather data handler built to learn how to:
- Work with REST APIs
- Parse and navigate nested JSON data
- Structure reusable functions
- Prepare data to be consumed by other applications

The goal is to use this project as a **data layer** for a future Mars dashboard app (e.g. Flutter or web).

---

## ✨ Current Features

- Fetch Mars weather data from NASA’s InSight API
- Retrieve all available Martian Sols
- Automatically determine the most recent Sol
- Extract weather data for a specific Sol
- Get:
  - Average temperature
  - Current Martian season
  - Most common wind direction
  - Average wind speed

Each piece of data is handled by its own function for clarity and reuse.

---

## 🧱 Tech Stack

- **Python 3.9+**
- **Requests** – HTTP requests to the NASA API
- **python-dotenv** – Environment variable management for API keys

---

## 🗂 Project Structure (High-Level)

- `main.py` – main script containing all logic
- `.env` – stores the NASA API key

### Key Functions
- `get_mars_data()` – fetch full weather dataset
- `get_available_sols(data)` – list all available Sols
- `get_current_sol(data)` – get the most recent Sol
- `get_sol_data(data, sol)` – retrieve data for a specific Sol
- `get_sol_temperature(sol_data)` – get average temperature
- `get_sol_season(sol_data)` – get current Martian season
- `get_sol_wind_direction(sol_data)` – get dominant wind direction
- `get_sol_wind_speed(sol_data)` – get average wind speed

---

## 🎯 Improvements / Learning Goals

- Turn this project into a data provider for a Mars weather dashboard app
- Expose the data through a simple API or service
- Format data into clean, app-friendly responses
- Improve error handling for missing or incomplete Sol data
- Gradually refactor into a more structured and scalable design

---
