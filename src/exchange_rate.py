from fredapi import Fred
import pandas as pd
from datetime import date, timedelta
from fred_api_key import fred
import plotly.express as px

class SpotRate():
    def __init__(self) -> None:
        pass

    class YENxUSD():
        def __init__(self) -> None:
            self.key = 'DEXJPUS'
            self.column_title = 'Japanese Yen to One USD'
            self.title = 'Japanese Yen to U.S. Dollar Spot Exchange Rate'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
            
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def one_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def two_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
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

    class REALxUSD():
        def __init__(self) -> None:
            self.key = 'DEXBZUS'
            self.column_title = 'Brazilian Reals to One USD'
            self.title = 'Brazilian Reals to U.S. Dollar Spot Exchange Rate'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
            
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def one_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def two_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
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

    class INDxUSD():
        def __init__(self) -> None:
            self.key = 'DEXINUS'
            self.column_title = 'Indian Rupees to One USD'
            self.title = 'Indian Rupees to U.S. Dollar Spot Exchange Rate'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
            
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def one_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def two_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
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

    class HKDxUSD():
        '''Hong Kong Dollars to U.S. Dollar Spot Exchange Rate'''
        def __init__(self) -> None:
            self.key = 'DEXHKUS'
            self.column_title = 'Hong Kong Dollars to One USD'
            self.title = 'Hong Kong Dollars to U.S. Dollar Spot Exchange Rate'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
            
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def one_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def two_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
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

    class THBxUSD():
        def __init__(self) -> None:
            self.key = 'DEXTHUS'
            self.column_title = 'Thai Baht to One USD'
            self.title = ' Thai Baht to U.S. Dollar Spot Exchange Rate'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
            
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def one_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def two_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
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

    class SKWxUSD():
        def __init__(self) -> None:
            self.key = 'DEXKOUS'
            self.column_title = 'South Korean Won to One USD'
            self.title = 'South Korean Won to U.S. Dollar Spot Exchange Rate'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
            
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def one_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def two_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
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

    class SLRxUSD():
        def __init__(self) -> None:
            self.key = 'DEXSLUS'
            self.column_title = 'Sri Lankan Rupees to One USD'
            self.title = 'Sri Lankan Rupees to U.S. Dollar Spot Exchange Rate'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
            
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def one_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def two_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
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

    class SFxUSD():
        def __init__(self) -> None:
            self.key = 'DEXSZUS'
            self.column_title = 'Swiss Francs to One USD'
            self.title = 'Swiss Francs to U.S. Dollar Spot Exchange Rate'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
            
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def one_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def two_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
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

    class TWDxUSD():
        def __init__(self) -> None:
            self.key = 'DEXTAUS'
            self.column_title = 'Taiwan Dollars to One USD'
            self.title = 'Taiwan Dollars to U.S. Dollar Spot Exchange Rate'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
            
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def one_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def two_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
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

    class RANDxUSD():
        def __init__(self) -> None:
            self.key = 'DEXSFUS'
            self.column_title = 'South African Rand to One USD'
            self.title = 'South African Rand to U.S. Dollar Spot Exchange Rate'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
            
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def one_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def two_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
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

    class MXPxUSD():
        def __init__(self) -> None:
            self.key = 'DEXMXUS'
            self.column_title = 'Mexican Pesos to One USD'
            self.title = 'Mexican Pesos to U.S. Dollar Spot Exchange Rate'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
            
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def one_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def two_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
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

    class USDxEURO():
        def __init__(self) -> None:
            self.key = 'DEXUSEU'
            self.column_title = 'USD to EURO'
            self.title = 'U.S. Dollars to Euro Spot Exchange Rate'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
            
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def one_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def two_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
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

    class USDxGBP():
        def __init__(self) -> None:
            self.key = 'DEXUSUK'
            self.column_title = 'USD to GBP'
            self.title = 'U.S. Dollars to U.K. Pound Sterling Spot Exchange Rate'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
            
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def one_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def two_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
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

    class USDxNZD():
        def __init__(self) -> None:
            self.key = 'DEXUSNZ'
            self.column_title = 'USD to NZD'
            self.title = 'U.S. Dollars to New Zealand Dollar Spot Exchange Rate'
        
        def plot(self, time_series:pd.DataFrame)->None:
            self.fig = px.line(time_series).update_layout(title=f'{self.title}', legend_title='', title_font_family="Raleway")
            self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
            self.fig.show()
            
        def global_price(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def one_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
            return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        def two_week_data(self)->pd.DataFrame:
            self.data=fred.get_series(self.key, observation_start=(date.today() - timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
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

