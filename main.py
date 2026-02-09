from fastapi import FastAPI
from app.commands import Commands

app = FastAPI()

app.get("/{sol}")
def main(sol: str):
    Commands.get_sol_data(sol)
        
if __name__ == "__main__":
    main()