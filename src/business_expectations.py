from fredapi import Fred
import pandas as pd
from datetime import date, timedelta
from fred_api_key import fred
import plotly.express as px

class BusinessExpectations():
    def __init__(self) -> None:
        pass
    
    class SalesGrowthRevenue():
        def __init__(self) -> None:
            self.key = 'ATLSBUSRGEP'
            self.column_title = 'Percent'
            self.title = ' Business Expectations: Sales Revenue Growth'
            self.max_date = '12/01/2016'
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

        def two_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=730)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def three_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def four_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=1460)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def five_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

    class EmploymentGrowth():
        def __init__(self) -> None:
            self.key = 'ATLSBUEGEP'
            self.column_title = 'Percent'
            self.title = ' Business Expectations: Employment Growth'
            self.max_date = '12/01/2016'
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

        def two_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=730)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def three_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def four_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=1460)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def five_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

class BusinessUncertainty():
    def __init__(self) -> None:
        pass
    
    class SalesGrowthRevenue():
        def __init__(self) -> None:
            self.key = 'ATLSBUSRGUP'
            self.column_title = 'Percent'
            self.title = 'Business Uncertainty: Sales Revenue Growth'
            self.max_date = '12/01/2016'
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

        def two_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=730)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def three_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def four_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=1460)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def five_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

    class EmploymentGrowth():
        def __init__(self) -> None:
            self.key = 'ATLSBUEGUP'
            self.column_title = 'Percent'
            self.title = ' Business Uncertainty: Employment Growth'
            self.max_date = '12/01/2016'
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

        def two_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=730)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def three_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def four_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=1460)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def five_year_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
