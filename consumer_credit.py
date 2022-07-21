from fredapi import Fred
import pandas as pd
from datetime import date
from fred_api_key import fred

class Credit():
    def __init__(self):
        pass
    def total_credit_owned(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Total Consumer Credit Owned and Securitized'''
        self.data = fred.get_series('TOTALSL', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Billions of Dollars']) 
    def student_loans(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Student Loans Owned and Securitized'''
        self.data = fred.get_series('SLOAS',observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Billions of Dollars'])
    def credit_card_rates(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Commercial Bank Interest Rate on Credit Card Plans, All Accounts'''
        self.data = fred.get_series('TERMCBCCALLNS', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Percent'])
    def vroom(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Motor Vehicle Loans Owned and Securitized'''
        self.data = fred.get_series('MVLOAS', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Billions of Dollars'])
    def revolving_credit(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Percent Change of Total Revolving Consumer Credit'''
        self.data = fred.get_series('REVOLSLAR', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Percentage Change at Annual Rate'])
    def fed_owned(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Total Consumer Credit Owned by the Federal Government (U.S.)'''
        self.data = fred.get_series('TOTALGOV', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Billions of Dollars'])
    def tcu_owned(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Total Consumer Credit Owned by Credit Unions'''
        self.data = fred.get_series('TOTALTCU', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Billions of Dollars'])
    def nfc_owned(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Total Consumer Credit Owned by Nonfinancial Business'''
        self.data = fred.get_series('TOTALNFC', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Billions of Dollars'])
    def di_owned(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Total Consumer Credit Owned by Depository Institutions'''
        self.data = fred.get_series('TOTALDI', observation_start=observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Billions of Dollars'])
    def fc_owned(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Total Consumer Credit Owned by Finance Companies'''
        self.data = fred.get_series('TOTALFC', observation_start=observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Billions of Dollars'])
    def bank_credit(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Bank Credit, All Commercial Banks'''
        self.data = fred.get_series('TOTBKCR', observation_start=observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Billions of Dollars'])

