import pandas as pd
from fredapi import Fred
from datetime import date
from fred_api_key import fred


class Housing():
    def __init__(self) -> None:
        pass
    def ZHVI(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Zillow Home Value Index for All Homes Including Single-Family Residences, Condos, and CO-OPs in the United States of America'''
        self.data = fred.get_series('USAUCSFRCONDOSMSAMID', observation_start = observation_start, observation_end = observation_end)
        return pd.DataFrame(self.data, columns=['Dollars'])
    def existing_home_sales(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Existing Home Sales'''
        self.data = fred.get_series('EXHOSLUSM495S', observation_start = observation_start, observation_end = observation_end)
        return pd.DataFrame(self.data, columns=['Number of Units'])
    def new_home_sales(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''New Privately-Owned Housing Units Started: Total Units'''
        self.data = fred.get_series('HOUST', observation_start = observation_start, observation_end = observation_end)
        return pd.DataFrame(self.data, columns=['Thousands of Units'])
    def housing_inventory(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Existing Home Sales: Housing Inventory'''
        self.data = fred.get_series('HOSINVUSM495N', observation_start = observation_start, observation_end = observation_end)
        return pd.DataFrame(self.data, columns=['Number of Units'])
    def HAI(self, observation_start='01/01/2021', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Housing Affordability Index (Fixed)'''
        self.data = fred.get_series('FIXHAI', observation_start = observation_start, observation_end = observation_end)
        return pd.DataFrame(self.data, columns=['Index'])
    def case_shiller(self, observation_start='01/01/1987', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        ''' S&P/Case-Shiller U.S. National Home Price Index'''
        self.data = fred.get_series('CSUSHPINSA', observation_start = observation_start, observation_end = observation_end)
        return pd.DataFrame(self.data, columns=['Index Jan 2000=100'])

class MortgageRate():
    def __init__(self) -> None:
        pass
    def thirty_year(self, observation_start='01/01/1970', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''30-Year Fixed Rate Mortgage Average in the United States'''
        self.data = fred.get_series('MORTGAGE30US', observation_start = observation_start, observation_end = observation_end)
        return pd.DataFrame(self.data, columns=['Percent'])
    def fifteen_year(self, observation_start='01/01/1970', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        ''' 15-Year Fixed Rate Mortgage Average in the United States'''
        self.data = fred.get_series('MORTGAGE15US', observation_start = observation_start, observation_end = observation_end)
        return pd.DataFrame(self.data, columns=['Percent'])