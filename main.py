from fastapi import FastAPI
from app.commands import Commands

app = FastAPI()

app.get("/{sol}")
def main(sol: str):
    sol_obj = Commands.get_sol_data(sol)
    return sol_obj.__dict__
        
if __name__ == "__main__":
    main()