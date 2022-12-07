from fredapi import Fred
import pandas as pd
from datetime import date, timedelta
from fred_api_key import fred
import plotly.express as px

class Credit():
    def __init__(self) -> None:
        pass

    class TotalCreditOwned():
        '''
        Total Consumer Credit Owned and Securitized
        '''
        def __init__(self) -> None:
            self.key = 'TOTALSL'
            self.column_title = 'Billions of Dollars'
            self.title = 'Total Consumer Credit Owned and Securitized'

        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
        
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start='01/01/1943', observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def one_month_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def two_month_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=60)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def three_month_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        def six_month_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def one_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        def three_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def five_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        def ten_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def fifteen_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=5475)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        def twenty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=7300)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

    class StudentLoans():
        '''
        Student Loans Owned and Securitized
        '''
        def __init__(self) -> None:
            self.key = 'SLOAS'
            self.column_title = 'Billions of Dollars'
            self.title = ''
    
    class MotorVehicleLoans():
        '''
        Motor Vehicle Loans Owned and Securitized
        '''
        def __init__(self) -> None:
            self.key = 'MVLOAS'
            self.column_title = 'Billions of Dollars'
            self.title = ''

    class RevolvingCredit():
        '''
        Percent Change of Total Revolving Consumer Credit
        '''
        def __init__(self) -> None:
            self.key = 'REVOLSLAR'
            self.column_title = 'Percentage Change at Annual Rate'
            self.title = ''

    class FederalOwnedDebt():
        '''
        Total Consumer Credit Owned by the Federal Government (U.S.)
        '''
        def __init__(self) -> None:
            self.key = 'TOTALGOV'
            self.column_title = 'Billions of Dollars'
            self.title = ''
    
    class CreditUnionOwnedDebt():
        '''
        Total Consumer Credit Owned by Credit Unions
        '''
        def __init__(self) -> None:
            self.key = 'TOTALTCU'
            self.column_title = 'Billions of Dollars'
            self.title = ''
    
    class DepositoryOwnedDebt():
        '''
        Total Consumer Credit Owned by Depository Institutions
        '''
        def __init__(self) -> None:
            self.key = 'TOTALDI'
            self.column_title = 'Billions of Dollars'
            self.title = ''

    class FinanceCompanyOwnedDebt():
        '''
        Total Consumer Credit Owned by Finance Companies
        '''
        def __init__(self) -> None:
            self.key = 'TOTALFC'
            self.column_title = 'Billions of Dollars'
            self.title = ''
    
    class BankOwnedDebt():
        '''
        Bank Credit, All Commercial Banks
        '''
        def __init__(self) -> None:
            self.key = 'TOTBKCR'
            self.column_title = 'Billions of Dollars'
            self.title = ''



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

