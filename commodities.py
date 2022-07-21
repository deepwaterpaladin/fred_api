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




