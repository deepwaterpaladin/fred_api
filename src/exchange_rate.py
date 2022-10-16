from fredapi import Fred
import pandas as pd
from datetime import date
from fred_api_key import fred


class SpotRate():
    def __init__(self) -> None:
        pass
    def CAD_USD(self, inverse=False, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Canadian Dollars to U.S. Dollar Spot Exchange Rate'''
        self.data = fred.get_series('DEXCAUS', observation_start = observation_start, observation_end=observation_end)
        if inverse == True:
            return pd.DataFrame(1/self.data, columns=['USD$ to CAD$'])
        else:
            return pd.DataFrame(self.data, columns=['CAD$ to USD$'])
    def YEN_USD(self, inverse=False, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Japanese Yen to U.S. Dollar Spot Exchange Rate'''
        self.data = fred.get_series('DEXJPUS', observation_start = observation_start, observation_end=observation_end)
        if inverse == True:
            return pd.DataFrame(1/self.data, columns=['USD$ to Yen'])    
        else:
            return pd.DataFrame(self.data, columns=['YEN to USD$'])
    def REAL_USD(self, inverse=False, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        ''' Brazilian Reals to U.S. Dollar Spot Exchange Rate'''
        self.data = fred.get_series('DEXBZUS', observation_start = observation_start, observation_end=observation_end)
        if inverse == True:
            return pd.DataFrame(1/self.data, columns=['USD$ to Reals'])
        else:
            return pd.DataFrame(self.data, columns=['Reals to USD$'])
    def IND_USD(self, inverse=False, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Indian Rupees to U.S. Dollar Spot Exchange Rate'''
        self.data = fred.get_series('DEXINUS', observation_start = observation_start, observation_end=observation_end)
        if inverse == True:
            return pd.DataFrame(1/self.data, columns=['USD$ to Rupees'])
        else:
            return pd.DataFrame(self.data, columns=['Rupees to USD$'])
    def HKD_USD(self, inverse=False, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Hong Kong Dollars to U.S. Dollar Spot Exchange Rate'''
        self.data = fred.get_series('DEXHKUS', observation_start = observation_start, observation_end=observation_end)
        if inverse == True:
            return pd.DataFrame(1/self.data, columns=['USD$ to HKD'])
        else:
            return pd.DataFrame(self.data, columns=['HKD to USD$'])
    def THB_USD(self, inverse=False, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Thai Baht to U.S. Dollar Spot Exchange Rate'''
        self.data = fred.get_series('DEXTHUS', observation_start = observation_start, observation_end=observation_end)
        if inverse == True:
            return pd.DataFrame(1/self.data, columns=['USD$ to Baht'])
        else:
            return pd.DataFrame(self.data, columns=['Baht to USD$'])
    def SKW_USD(self, inverse=False, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''South Korean Won to U.S. Dollar Spot Exchange Rate'''
        self.data = fred.get_series('DEXKOUS', observation_start = observation_start, observation_end=observation_end)
        if inverse == True:
            return pd.DataFrame(1/self.data, columns=['USD$ to Won'])
        else:
            return pd.DataFrame(self.data, columns=['Won to USD$'])
    def SLR_USD(self, inverse=False, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Sri Lankan Rupees to U.S. Dollar Spot Exchange Rate'''
        self.data = fred.get_series('DEXSLUS', observation_start = observation_start, observation_end=observation_end)
        if inverse == True:
            return pd.DataFrame(1/self.data, columns=['USD$ to Rupees'])
        else:
            return pd.DataFrame(self.data, columns=['Rupees to USD$'])
    def SF_USD(self, inverse=False, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        ''' Swiss Francs to U.S. Dollar Spot Exchange Rate'''
        self.data = fred.get_series('DEXSZUS', observation_start = observation_start, observation_end=observation_end)
        if inverse == True:
            return pd.DataFrame(1/self.data, columns=['USD$ to Francs'])
        else:
            return pd.DataFrame(self.data, columns=['Francs to USD$'])
    def TWD_USD(self, inverse=False, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Taiwan Dollars to U.S. Dollar Spot Exchange Rate'''
        self.data = fred.get_series('DEXTAUS', observation_start = observation_start, observation_end=observation_end)
        if inverse == True:
            return pd.DataFrame(1/self.data, columns=['USD$ to Taiwan Dollars'])
        else:
            return pd.DataFrame(self.data, columns=['Taiwan Dollars to USD$'])
    def RAND_USD(self, inverse=False, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''South African Rand to U.S. Dollar Spot Exchange Rate'''
        self.data = fred.get_series('DEXSFUS', observation_start = observation_start, observation_end=observation_end)
        if inverse == True:
            return pd.DataFrame(1/self.data, columns=['USD$ to Rands'])
        else:
            return pd.DataFrame(self.data, columns=['Rands to USD$'])
    def MXP_USD(self, inverse=False, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Mexican Pesos to U.S. Dollar Spot Exchange Rate'''
        self.data = fred.get_series('DEXMXUS', observation_start = observation_start, observation_end=observation_end)
        if inverse == True:
            return pd.DataFrame(1/self.data, columns=['USD$ to Pesos'])
        else:
            return pd.DataFrame(self.data, columns=['Pesos to USD$'])
    def USD_EURO(self, inverse=False, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''U.S. Dollars to Euro Spot Exchange Rate'''
        self.data = fred.get_series('DEXUSEU', observation_start = observation_start, observation_end=observation_end)
        if inverse == True:
            return pd.DataFrame(1/self.data, columns=['Euro to USD$'])
        else:
            return pd.DataFrame(self.data, columns=['USD$ to One Euro'])
    def USD_GBP(self, inverse=False, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''U.S. Dollars to U.K. Pound Sterling Spot Exchange Rate'''
        self.data = fred.get_series('DEXUSUK', observation_start = observation_start, observation_end=observation_end)
        if inverse == True:
            return pd.DataFrame(1/self.data, columns=['GBP to USD$'])
        else:
            return pd.DataFrame(self.data, columns=['USD$ to GBP'])
    def USD_NZD(self, inverse=False, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''U.S. Dollars to New Zealand Dollar Spot Exchange Rate'''
        self.data = fred.get_series('DEXUSNZ', observation_start = observation_start, observation_end=observation_end)
        if inverse == True:
            return pd.DataFrame(1/self.data, columns=['NZD to USD$'])
        else:
            return pd.DataFrame(self.data, columns=['USD$ to NZD'])
    