class Sol:
    def __init__(self, temperature, season, wind_direction, wind_speed):
        self.temperature = temperature
        self.season = season
        self.wind_direction = wind_direction
        self.wind_speed = wind_speed

    def __str__(self):
        return f'''
        Temperature = {self.temperature}
        Season = {self.season}
        Wind Direction = {self.wind_direction}
        Wind Speed = {self.wind_speed}
        '''