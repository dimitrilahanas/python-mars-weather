from mars_data import MarsData
from models.sol import Sol

class Commands:
    mars_data = MarsData.get_mars_data()

    @staticmethod
    def get_available_sols():
        data = Commands.mars_data
        return data["sol_keys"]

    @staticmethod
    def get_current_sol():
        data = Commands.mars_data
        return data["sol_keys"][-1]
    
    @staticmethod
    def get_sol_data(sol_num: str):
        data = Commands.mars_data[sol_num]
        return Sol (
            temperature=data["AT"]["av"],
            season=data["Season"],
            wind_direction=data["WD"]["most_common"]["compass_point"],
            wind_speed=["HWS"]["av"]
        )