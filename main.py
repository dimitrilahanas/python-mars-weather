from fastapi import FastAPI
from app.commands import Commands

app = FastAPI()

@app.get("/available")
def get_available_sols():
    return {"available_sols": Commands.get_available_sols()}

@app.get("/{sol}")
def get_sol_data(sol: str):
    sol_obj = Commands.get_sol_data(sol)
    return sol_obj.__dict__