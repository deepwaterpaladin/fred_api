from fredapi import Fred
import pandas as pd
from datetime import date, timedelta
import plotly.express as px
from fred_api_key import fred

class M2():
    def __init__(self):
        '''M2, Monthly'''
        self.key = 'M2SL'
        self.column_title = 'Billions of US Dollars'
    
    def plot(self, time_series:pd.DataFrame)->None:
        self.fig = px.line(time_series).update_layout(title='M2', legend_title='', title_font_family="Raleway")
        self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='Billions of Dollars')
        self.fig.show()
    
    def one_month_data(self)->pd.DataFrame:
        self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
        return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
    
    def three_month_data(self)->pd.DataFrame:
        self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
        return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

    def six_month_data(self)->pd.DataFrame:
        self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
        return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
    
    def one_year_data(self)->pd.DataFrame:
        self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
        return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

    def three_year_data(self)->pd.DataFrame:
        self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
        return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
    
    def five_year_data(self)->pd.DataFrame:
        self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
        return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

    def ten_year_data(self)->pd.DataFrame:
        self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=3652)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
        return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
    
    def fifteen_year_data(self)->pd.DataFrame:
        self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=5478)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
        return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
    
    def twenty_year_data(self)->pd.DataFrame:
        self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=7305)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
        return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

    def thirty_year_data(self)->pd.DataFrame:
        self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=10956)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
        return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
    
    def fourty_year_data(self)->pd.DataFrame:
        self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14610)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
        return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
    
    def fifty_year_data(self)->pd.DataFrame:
        self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=18260)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
        return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

    def total(self)->pd.DataFrame:
        self.data=fred.get_series(self.key, observation_start='01/01/1960', observation_end=date.today().strftime("%m/%d/%Y"))
        return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
