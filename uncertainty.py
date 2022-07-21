import pandas as pd
from fredapi import Fred
from datetime import date
from fred_api_key import fred

class UncertaintyIndex():
    def __init__(self) -> None:
        pass
    def EUI_USA(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))-> pd.DataFrame:
        '''Economic Policy Uncertainty Index for United States'''
        self.data = fred.get_series('USEPUINDXD', observation_start = observation_start, observation_end = observation_end)
        return pd.DataFrame(self.data, columns=['Index'])
    def EME_USA(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))-> pd.DataFrame:
        '''Equity Market-related Economic Uncertainty Index'''
        self.data = fred.get_series('WLEMUINDXD', observation_start = observation_start, observation_end = observation_end)
        return pd.DataFrame(self.data, columns=['Index'])
    def EUI_MP(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))-> pd.DataFrame:
        '''Economic Policy Uncertainty Index: Categorical Index: Monetary policy'''
        self.data = fred.get_series('EPUMONETARY', observation_start = observation_start, observation_end = observation_end)
        return pd.DataFrame(self.data, columns=['Index'])
        