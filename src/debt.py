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
            self.max_date = '01/01/1943'
            self.frequency = 'Monthly'

        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
        
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=self.max_date, observation_end=date.today().strftime("%m/%d/%Y"))
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
        
        def thirty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=10950)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def forty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14600)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        def fifty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=18250)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

    class StudentLoans():
        '''
        Student Loans Owned and Securitized
        '''
        def __init__(self) -> None:
            self.key = 'SLOAS'
            self.column_title = 'Billions of Dollars'
            self.title = 'Student Loans Owned and Securitized'
            self.max_date = '01/01/2006'
            self.frequency = 'Quarterly, End of Period'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
        
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=self.max_date, observation_end=date.today().strftime("%m/%d/%Y"))
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
    
    class MotorVehicleLoans():
        '''
        Motor Vehicle Loans Owned and Securitized
        '''
        def __init__(self) -> None:
            self.key = 'MVLOAS'
            self.column_title = 'Billions of Dollars'
            self.title = 'Motor Vehicle Loans Owned and Securitized'
            self.max_date = '01/01/1943'
            self.frequency = 'Quarterly, End of Period'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
        
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=self.max_date, observation_end=date.today().strftime("%m/%d/%Y"))
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

        def thirty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=10950)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def forty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14600)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        def fifty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=18250)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

    class RevolvingCredit():
        '''
        Percent Change of Total Revolving Consumer Credit
        '''
        def __init__(self) -> None:
            self.key = 'REVOLSLAR'
            self.column_title = 'Percentage Change at Annual Rate'
            self.title = 'Percent Change of Total Revolving Consumer Credit'
            self.max_date = '02/01/1962'
            self.frequency = 'Monthly'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
        
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=self.max_date, observation_end=date.today().strftime("%m/%d/%Y"))
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

        def thirty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=10950)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def forty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14600)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def fifty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=18250)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

    class FederalOwnedDebt():
        '''
        Total Consumer Credit Owned by the Federal Government (U.S.)
        '''
        def __init__(self) -> None:
            self.key = 'TOTALGOV'
            self.column_title = 'Billions of Dollars'
            self.title = 'Total Consumer Credit Owned by Federal Government'
            self.max_date = '01/01/1977'
            self.frequency = 'Monthly'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
        
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=self.max_date, observation_end=date.today().strftime("%m/%d/%Y"))
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

        def thirty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=10950)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def forty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14600)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        def fifty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=18250)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
    
    class CreditUnionOwnedDebt():
        '''
        Total Consumer Credit Owned by Credit Unions
        '''
        def __init__(self) -> None:
            self.key = 'TOTALTCU'
            self.column_title = 'Billions of Dollars'
            self.title = 'Total Consumer Credit Owned by Credit Unions'
            self.max_date = '01/01/1943'
            self.frequency = 'Monthly'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
        
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=self.max_date, observation_end=date.today().strftime("%m/%d/%Y"))
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

        def thirty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=10950)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def forty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14600)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        def fifty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=18250)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
    
    class DepositoryOwnedDebt():
        '''
        Total Consumer Credit Owned by Depository Institutions
        '''
        def __init__(self) -> None:
            self.key = 'TOTALDI'
            self.column_title = 'Billions of Dollars'
            self.title = 'Total Consumer Credit Owned by Depository Institutions'
            self.max_date = '01/01/1943'
            self.frequency = 'Monthly'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
        
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=self.max_date, observation_end=date.today().strftime("%m/%d/%Y"))
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

        def thirty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=10950)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def forty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14600)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        def fifty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=18250)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

    class FinanceCompanyOwnedDebt():
        '''
        Total Consumer Credit Owned by Finance Companies
        '''
        def __init__(self) -> None:
            self.key = 'TOTALFC'
            self.column_title = 'Billions of Dollars'
            self.title = 'Total Consumer Credit Owned by Finance Companies'
            self.max_date = '01/01/1943'
            self.frequency = 'Monthly'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
        
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=self.max_date, observation_end=date.today().strftime("%m/%d/%Y"))
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

        def thirty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=10950)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def forty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14600)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def fifty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=18250)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
    
    class BankOwnedDebt():
        '''
        Bank Credit, All Commercial Banks
        '''
        def __init__(self) -> None:
            self.key = 'TOTBKCR'
            self.column_title = 'Billions of Dollars'
            self.title = 'Bank Credit, All Commercial Banks'
            self.max_date = '01/01/1973'
            self.frequency = 'Weekly, Ending Wednesday'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
        
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=self.max_date, observation_end=date.today().strftime("%m/%d/%Y"))
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

        def thirty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=10950)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def forty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14600)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

    class NonfinanceCompanyOwnedDebt():
        '''
        Total Consumer Credit Owned by Nonfinancial Business
        '''
        def __init__(self) -> None:
            self.key = 'TOTALNFC'
            self.column_title = 'Billions of Dollars'
            self.title = 'Total Consumer Credit Owned by Nonfinancial Business'
            self.max_date = '01/01/1943'
            self.frequency = 'Monthly'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
        
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=self.max_date, observation_end=date.today().strftime("%m/%d/%Y"))
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

        def thirty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=10950)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def forty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14600)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def fifty_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=18250)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

