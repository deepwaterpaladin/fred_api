import pandas as pd
from fredapi import Fred
from src.fred_api_key import fred

class SP500():
    def __init__(self) -> None:
        pass
    def get_index(self, observation_start='01/01/1985', observation_end='07/19/2022')-> pd.DataFrame:
        '''S&P 500'''
        self.data = fred.get_series('SP500', observation_start = observation_start, observation_end = observation_end)
        return pd.DataFrame(self.data, columns=['Index'])