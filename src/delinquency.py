from fredapi import Fred
import pandas as pd
from datetime import date
from src.fred_api_key import fred

class Delinquency():
    def __init__(self):
        pass
    def credit_cards(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('DRCCLACBS', observation_start=observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Delinquency Rate'])
    def single_family_mortgages(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('DRSFRMACBS', observation_start=observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Delinquency Rate'])
    def all_loans(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('DRALACBN', observation_start=observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Delinquency Rate'])
    def consumer_loans(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('DRCLACBS', observation_start=observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Delinquency Rate'])
    def business_loans(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('DRBLACBS', observation_start=observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Delinquency Rate'])
    def commercial_real_estate_loans(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('DRCRELEXFACBS', observation_start=observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Delinquency Rate'])
    def other_consumer_loans(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        self.data = fred.get_series('DROCLACBS', observation_start=observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Delinquency Rate'])
    def secured_loans(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Delinquency Rate on Loans Secured by Real Estate, All Commercial Banks'''
        self.data = fred.get_series('DRSREACBS', observation_start=observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Delinquency Rate'])
    