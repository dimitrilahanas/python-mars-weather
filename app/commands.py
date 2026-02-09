from mars_data import MarsData

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
    def get_sol_temperature(sol: str):
        data = Commands.mars_data
        sol_data = data[sol]
        temperature = sol_data["AT"]
        return f'{temperature["av"]} degrees C'

    @staticmethod
    def get_sol_season(sol: str):
        data = Commands.mars_data
        sol_data = data[sol]
        return sol_data["Season"]

    @staticmethod
    def get_sol_wind_direction(sol: str):
        data = Commands.mars_data
        sol_data = data[sol]
        wind = sol_data["WD"]
        wind_direction = wind["most_common"]
        return wind_direction["compass_point"]

    @staticmethod
    def get_sol_wind_speed(sol: str):
        data = Commands.mars_data
        sol_data = data[sol]
        horizontal_speed = sol_data["HWS"]
        return f'{horizontal_speed["av"]} m/s'