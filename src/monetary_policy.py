from fredapi import Fred
import pandas as pd
from datetime import date
from fred_api_key import fred

class MB():
    def __init__(self):
        pass
    def monetary_base(self, observation_start='01/01/1960', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Monetary Base; Total, Monthly'''
        self.data = fred.get_series('BOGMBASE', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Millions of Dollars'])
    def mb_currency(self, observation_start='01/01/1960', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Monetary Base; Currency in Circulation, Monthly'''
        self.data = fred.get_series('MBCURRCIR', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Ratio'])
    def mb_reserve(self, observation_start='01/01/1960', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Monetary Base; Reserve Balances'''
        self.data = fred.get_series('BOGMBBM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Millions of Dollars'])
    def swiss_mb(self, observation_start='01/01/1960', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Swiss Monetary Base Aggregate'''
        self.data = fred.get_series('SNBMONTBASE', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['CHF Millions'])

class M1():
    def __init__(self):
        pass
    def m1(self, observation_start='01/01/1960', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''M1, Quarterly'''
        self.data = fred.get_series('M1SL', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Billions of Dollars'])
    def m1_velo(self, observation_start='01/01/1960', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Velocity of M1 Money Stock, Quarterly'''
        self.data = fred.get_series('M1V', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Ratio'])

class M2():
    def __init__(self):
        pass
    def m2(self, observation_start='01/01/1960', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''M2, Quarterly'''
        self.data = fred.get_series('M1SL', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Billions of Dollars'])
    def m2_velo(self, observation_start='01/01/1960', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        ''' Velocity of M2 Money Stock, Quarterly'''
        self.data = fred.get_series('M1V', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Ratio'])
