# Python-Mars-Weather

A Python script to fetch and explore Mars weather data from NASA’s InSight lander API.  
⚠️ Note: This project is for learning purposes.  
I created it while learning Python and working with APIs, so the code may be simple or not fully optimized.  
Use it as a reference for my learning journey, not as production-ready code.

---

## 📌 About the Project

This project is a beginner-friendly Python script built to learn how to:  
- Fetch data from a public API  
- Parse JSON data in Python  
- Work with nested dictionaries  
- Build modular functions for data extraction  

The script allows users to get available Martian days (Sols), retrieve data for a specific Sol, and extract temperature information.

---

## ✨ Features

- Fetch Mars weather data from NASA’s InSight API  
- List available Martian Sols  
- Get the latest Sol automatically  
- Extract average, minimum, and maximum temperatures for a Sol  
- Modular functions for easy expansion  

---

## 🧱 Tech Stack

- **Python 3.9+**  
- **Requests** (for HTTP API calls)  
- **python-dotenv** (for storing API keys)  

---

## 🗂 Project Structure (High-Level)

- `main.py` – main script file  
- `.env` – stores NASA API key  
- Functions include:  
  - `get_mars_data()` – fetch full dataset  
  - `get_available_sols(data)` – list all Sols  
  - `get_current_sol(data)` – get latest Sol  
  - `get_sol_data(data, sol)` – get data for a specific Sol  
  - `get_sol_temperature(sol_data)` – extract temperature info  

---

## 🎯 Improvements / Learning Goals

- Turn this script into something that can provide data to an app, which will be a Mars dashboard  
