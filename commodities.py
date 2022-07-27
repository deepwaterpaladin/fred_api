from fredapi import Fred
import pandas as pd
from datetime import date
from fred_api_key import fred

class Commodity():
    def __init__(self)->pd.DataFrame:
        pass
    def wheat(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PWHEAMTUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def barley(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PBARLUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def corn(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PMAIZMTUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def iron_ore(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PIORECRUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def aluminum(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PALUMUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def copper(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Global price of Copper, Monthly'''
        self.data = fred.get_series('PCOPPUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['U.S. Dollars per Ton'])
    def metal_index(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PMETAINDEXM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def soybeans(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PSOYBUSDQ', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def shrimp(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PSHRIUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def beef(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PBEEFUSDQ', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def bananas(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PBANSOPUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def cotton(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PCOTTINDUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def zinc(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PZINCUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def olive_oil(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('POLVOILUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def fish(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PSALMUSDA', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def shellfish(self, adjusted=False, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Producer Price Index by Commodity: Processed Foods and Feeds: Unprocessed Shellfish'''
        if adjusted == True:
            self.data = fred.get_series('WPS022305', observation_start = observation_start, observation_end=observation_end)
        else:
            self.data = fred.get_series('WPU022305', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Index December 1991 = 100'])
    def nickel(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PNICKUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def uranium(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PURANUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def us_lng(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('MNGLCP', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def coffee(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PCOFFOTMUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def poultry(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PPOULTUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def cocoa(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PCOCOUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def swine(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PPORKUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def lead(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PLEADUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def tin(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PTINUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])
    def lamb(self, observation_start='01/01/1985', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('PLAMBUSDM', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Price'])

class NaturalGas():
    def __init__(self) -> None:
        pass
    def spot_price(self, format='daily', observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Henry Hub Natural Gas Spot Price'''
        if format == 'monthly':
            self.data = fred.get_series('MHHNGSP', observation_start = observation_start, observation_end=observation_end)
        elif format == 'weekly':
            self.data = fred.get_series('WHHNGSP', observation_start = observation_start, observation_end=observation_end)
        elif format == 'annual' or format == 'yearly':
            self.data = fred.get_series('AHHNGSP', observation_start = observation_start, observation_end=observation_end)
        else:
            self.data = fred.get_series('DHHNGSP', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Dollars per Million BTUs'])
    def ppi(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Producer Price Index by Commodity: Fuels and Related Products and Power: Natural Gas '''
        self.data = fred.get_series('WPU0531', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Index 1982=100'])
    def ppi_to_consumers(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Producer Price Index by Industry: Natural Gas Distribution: Natural Gas to Ultimate Consumers (Monthly)'''
        self.data = fred.get_series('PCU22121022121011', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Index December 1990=100'])
    def consumption(self, adjusted=True, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Natural Gas Consumption'''
        if adjusted==True:
            self.data = fred.get_series('NATURALGASD11', observation_start = observation_start, observation_end = observation_end) # Seasonally Adjusted
        else:
            self.data = fred.get_series('NATURALGAS', observation_start = observation_start, observation_end = observation_end) # Non Seasonally Adjusted
        return pd.DataFrame(self.data, columns=['Billion Cubic Feet'])
    def LNG_composite_price(self, format='monthly', observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''U.S. Natural Gas Liquid Composite Price'''
        if format == 'annually' or format == 'yearly':
            self.data = fred.get_series('ANGLCP', observation_start = observation_start, observation_end = observation_end)
        else:
            self.data = fred.get_series('MNGLCP', observation_start = observation_start, observation_end = observation_end)
        return pd.DataFrame(self.data, columns=['Dollars per Million BTUs'])
    def capacity_utilization(self, format='monthly', observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Capacity Utilization: Utilities: Natural Gas Distribution (NAICS = 2212)'''
        if format == 'quarterly':
            self.data = fred.get_series('CAPUTLG2212SQ', observation_start = observation_start, observation_end = observation_end)
        else:
            self.data = fred.get_series('CAPUTLG2212S', observation_start = observation_start, observation_end = observation_end)
        return pd.DataFrame(self.data, columns=['Percent of Capacity'])


