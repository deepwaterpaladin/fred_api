import pandas as pd
from fredapi import Fred
from datetime import date
from src.fred_api_key import fred

class Unemployment():
    def __init__(self)-> None:
        pass
    def initial_claims(self, adjusted=True, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))-> pd.DataFrame:
        '''Initial Claims'''
        if adjusted==True:
            self.data = fred.get_series('ICSA', observation_start = observation_start, observation_end = observation_end) # Seasonally Adjusted
        else:
            self.data = fred.get_series('ICNSA', observation_start = observation_start, observation_end = observation_end) # Non Seasonally Adjusted
        return pd.DataFrame(self.data, columns=['Number'])
    def continued_claims(self, adjusted=True, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))-> pd.DataFrame:
        '''Continued Claims (Insured Unemployment)'''
        if adjusted==True:
            self.data = fred.get_series('CCSA', observation_start = observation_start, observation_end = observation_end) # Seasonally Adjusted
        else:
            self.data = fred.get_series('CCNSA', observation_start = observation_start, observation_end = observation_end) # Non Seasonally Adjusted
        return pd.DataFrame(self.data, columns=['Number'])
    def initial_claims_MA(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))-> pd.DataFrame:
        '''4-Week Moving Average of Initial Claims'''
        self.data = fred.get_series('IC4WSA', observation_start = observation_start, observation_end = observation_end)
        return pd.DataFrame(self.data, columns=["Number"])
    def continued_claims_MA(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))-> pd.DataFrame:
        '''4-Week Moving Average of Continued Claims (Insured Unemployment)'''
        self.data = fred.get_series('CC4WSA', observation_start = observation_start, observation_end = observation_end)
        return pd.DataFrame(self.data, columns=["Number"])