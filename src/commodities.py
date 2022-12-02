from datetime import date
from fred_api_key import fred
import pandas as pd
import plotly.express as px
import datetime


class Commodity():
    def __init__(self):
        pass
    
    class Metals():
        def __init__(self) -> None:
            pass
        
        class IronOre():
            def __init__(self) -> None:
                self.key = 'PIORECRUSDM'
                self.column_title = 'USD per Metric Tonne'

            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global Price of Iron Ore', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        class Aluminum():
            def __init__(self) -> None:
                self.key = 'PALUMUSDM'
                self.column_title = 'USD per Metric Tonne'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Aluminum', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Metric Ton')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        class Copper():
            def __init__(self) -> None:
                self.key = 'PCOPPUSDM'
                self.column_title = 'USD per Metric Tonne'

            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global Price of Copper', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        class Nickel():
            def __init__(self) -> None:
                self.key = 'PNICKUSDM'
                self.column_title = 'USD per Metric Tonne'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Nickel', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Metric Ton')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        class Zinc():
            def __init__(self) -> None:
                self.key = 'PZINCUSDM'
                self.column_title = 'USD per Metric Tonne'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Zinc', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Metric Ton')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        class Lead():
            def __init__(self) -> None:
                self.key = 'PLEADUSDM'
                self.column_title = 'USD per Metric Tonne'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Lead', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Metric Ton')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        class Tin():
            def __init__(self) -> None:
                self.key = 'PTINUSDM'
                self.column_title = 'USD per Metric Tonne'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Tin', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Metric Ton')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        class Uranium():
            def __init__(self) -> None:
                self.key = 'PURANUSDM'
                self.column_title = 'USD per Metric Tonne'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Uranium', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Metric Ton')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

    class Agriculture():
        def __init__(self) -> None:
            pass
        
        class Wheat():
            def __init__(self) -> None:
                ''' Global price of Wheat, U.S. Dollars per Metric Ton, Not Seasonally Adjusted'''
                self.key = 'PWHEAMTUSDM'
                self.column_title = 'USD per Metric Tonne'

            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global Price of Wheat', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        class Barley():
            def __init__(self) -> None:
                ''' Global price of Barley, U.S. Dollars per Metric Ton, Not Seasonally Adjusted '''
                self.key = 'PBARLUSDM'
                self.column_title = 'USD per Metric Tonne'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Barley', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Metric Ton')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        class Corn():
            def __init__(self) -> None:
                ''' Global price of Corn, U.S. Dollars per Metric Ton, Not Seasonally Adjusted '''
                self.key = 'PMAIZMTUSDM'
                self.column_title = 'USD per Metric Tonne'

            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global Price of Corn', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        class Soybeans():
            def __init__(self) -> None:
                self.key = 'PSOYBUSDQ'
                self.column_title = 'USD per Metric Tonne'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Soybeans', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Metric Ton')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        class Bananas():
            def __init__(self) -> None:
                self.key = 'PBANSOPUSDM'
                self.column_title = 'USD per Metric Tonne'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Bananas', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Metric Ton')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        class Cotton():
            def __init__(self) -> None:
                self.key = 'PCOTTINDUSDM'
                self.column_title = 'U.S. Cents per Pound'

            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global Price of Cotton', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        class OliveOil():
            def __init__(self) -> None:
                self.key = 'POLVOILUSDM'
                self.column_title = 'USD per Metric Tonne'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Olive Oil', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Metric Ton')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        class Coffee():
            def __init__(self) -> None:
                '''Global price of Coffee, Other Mild Arabica'''
                self.key = 'PCOFFOTMUSDM'
                self.column_title = 'US Cents per Pound'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Zinc', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Metric Ton')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        class Cocoa():
            def __init__(self) -> None:
                '''Global price of Cocoa'''
                self.key = 'PCOCOUSDM'
                self.column_title = 'USD per Metric Tonne'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Tin', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Metric Ton')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

    class Livestock():
        def __init__(self) -> None:
            pass

        class Shrimp():
            def __init__(self) -> None:
                self.key = 'PSHRIUSDM'
                self.column_title = 'USD per Kilogram'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Shrimp', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Kilogram')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        class Beef():
            def __init__(self) -> None:
                self.key = 'PBEEFUSDQ'
                self.column_title = 'U.S. Cents per Pound'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Beef', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='U.S. Cents per Pound')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        class Fish():
            def __init__(self) -> None:
                self.key = 'PSALMUSDA'
                self.column_title = 'USD per Metric Tonne'

            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global Price of Fish', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title=f'{self.column_title}')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        class Shellfish():
            def __init__(self) -> None:
                '''Producer Price Index by Commodity: Processed Foods and Feeds: Unprocessed Shellfish'''
                self.key = 'WPU022305'
                self.column_title = 'USD per Metric Tonne'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Shellfish', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Metric Ton')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        class Poultry():
            def __init__(self) -> None:
                self.key = 'PPOULTUSDM'
                self.column_title = 'US Cents per Pound'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Poultry', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Metric Ton')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

        class Swine():
            def __init__(self) -> None:
                self.key = 'PPORKUSDM'
                self.column_title = 'US Cents per Pound'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Swine', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Metric Ton')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
        
        class Lamb():
            def __init__(self) -> None:
                self.key = 'PLAMBUSDM'
                self.column_title = 'US Cents per Pound'
            
            def plot(self, time_series:pd.DataFrame)->None:
                self.fig = px.line(time_series).update_layout(title='Global price of Lamb', legend_title='', title_font_family="Raleway")
                self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars per Metric Ton')
                self.fig.show()

            def global_price(self, observation_start='01/02/1990', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                '''Global price of Aluminum'''
                self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def two_week_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def one_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def three_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def six_month_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def one_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def three_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
            
            def five_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            def ten_year_price(self)->pd.DataFrame:
                self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

    class Energy():
        def __init__(self) -> None:
            pass

        class Oil():
            def __init__(self) -> None:
                pass
        
            class WestTexasIntermediate():
                def __init__(self) -> None:
                    self.key = 'DCOILWTICO'

                def plot(self, time_series:pd.DataFrame)->None:
                    self.fig = px.line(time_series).update_layout(title='West Texas Intermediate, Price over time', legend_title='', title_font_family="Raleway")
                    self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars')
                    self.fig.show()

                def spot_price(self, observation_start='01/02/1986', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                    '''Crude Oil Prices: West Texas Intermediate (WTI) - Cushing, Oklahoma - Dollars per Barrel, Not Seasonally Adjusted '''
                    self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                    return pd.DataFrame(self.data,columns=['Price'])

                def one_week_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])
                
                def two_week_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])

                def one_month_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])
                
                def three_month_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])

                def six_month_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])
                
                def one_year_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])

                def three_year_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])
                
                def five_year_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])

                def ten_year_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])
            
            class BrentCrude():
                def __init__(self) -> None:
                    self.key = 'DCOILBRENTEU'
                
                def plot(self, time_series:pd.DataFrame)->None:
                    self.fig = px.line(time_series).update_layout(title='West Texas Intermediate, Price over time', legend_title='', title_font_family="Raleway")
                    self.fig.update_xaxes(title='Date', rangeselector_font_family="Times New Roman",rangeslider_visible=True).update_yaxes(title='United States Dollars')
                    self.fig.show()

                def spot_price(self, observation_start='01/02/1986', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                    '''Crude Oil Prices: Brent - Europe - Dollars per Barrel, Not Seasonally Adjusted '''
                    self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                    return pd.DataFrame(self.data,columns=['Price'])

                def one_week_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])
                
                def two_week_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])

                def one_month_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])
                
                def three_month_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])

                def six_month_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])
                
                def one_year_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])

                def three_year_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])
                
                def five_year_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])

                def ten_year_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=['Price'])

        class NaturalGas():
            def __init__(self) -> None:
                pass
            
            class USA():
                def __init__(self)->None:
                    self.key = 'DHHNGSP'
                    self.column_title = 'Dollars per Million BTUs'
                
                def consumption(self, adjusted=True, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                    '''Natural Gas Consumption'''
                    if adjusted==True:
                        self.data = fred.get_series('NATURALGASD11', observation_start = observation_start, observation_end = observation_end) # Seasonally Adjusted
                    else:
                        self.data = fred.get_series('NATURALGAS', observation_start = observation_start, observation_end = observation_end) # Non Seasonally Adjusted
                    return pd.DataFrame(self.data, columns=['Billion Cubic Feet'])

                def capacity_utilization(self, format='monthly', observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                    '''Capacity Utilization: Utilities: Natural Gas Distribution (NAICS = 2212)'''
                    if format == 'quarterly':
                        self.data = fred.get_series('CAPUTLG2212SQ', observation_start = observation_start, observation_end = observation_end)
                    else:
                        self.data = fred.get_series('CAPUTLG2212S', observation_start = observation_start, observation_end = observation_end)
                    return pd.DataFrame(self.data, columns=['Percent of Capacity'])

                def total_price(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
                
                def one_week_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
                
                def two_week_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=14)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

                def one_month_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
                
                def three_month_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

                def six_month_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
                
                def one_year_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

                def three_year_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
                
                def five_year_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

                def ten_year_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

            class EU():
                def __init__(self)->None:
                    self.key = 'PNGASEUUSDM'
                    self.column_title = 'Dollars per Million BTUs'
                
                def total_price(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start = observation_start, observation_end = observation_end)
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

                def one_month_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
                
                def three_month_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=91)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

                def six_month_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=182)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
                
                def one_year_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

                def three_year_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1095)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
                
                def five_year_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=1825)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])

                def ten_year_price(self)->pd.DataFrame:
                    self.data=fred.get_series(self.key, observation_start=(date.today() - datetime.timedelta(days=3650)).strftime("%m/%d/%Y"), observation_end=date.today().strftime("%m/%d/%Y"))
                    return pd.DataFrame(self.data,columns=[f'{self.column_title}'])
