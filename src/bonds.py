import pandas as pd
from datetime import date
from src.fred_api_key import fred

class CorporateBonds():
    def __init__(self):
        pass
    def AAA(self, timeframe = str, observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Moody's Seasoned Aaa Corporate Bond Yield (Weekly or Monthly)'''
        if timeframe == 'Weekly':
            self.data = fred.get_series('WAAA', observation_start='01/05/1962', observation_end=observation_end) # Weekly series
        elif timeframe == 'Daily':
            self.data = fred.get_series('DAAA', observation_start = '01/01/1985', observation_end = observation_end) # Daily series
        else:
            self.data = fred.get_series('AAA', observation_start='01/01/1919', observation_end=observation_end) # Monthly series
        return pd.DataFrame(self.data,columns=['Percent'])
    def BAA(self, timeframe = str, observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Moody's Seasoned Baa Corporate Bond Yield'''
        if timeframe == 'Weekly':
            self.data = fred.get_series('WBAA', observation_start='01/05/1962', observation_end=observation_end) # Weekly series
        elif timeframe == 'Daily':
            self.data = fred.get_series('DBAA', observation_start = '01/01/1985', observation_end = observation_end) # Daily series
        else:
            self.data = fred.get_series('BAA', observation_start='01/01/1919', observation_end=observation_end) # Monthly series
        return pd.DataFrame(self.data,columns=['Percent'])
    def AAA_to_10_Year(self, daily = True, observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Moody's Seasoned AAA Corporate Bond Yield Relative to Yield on 10-Year Treasury Constant Maturity (Daily or Monthly)'''
        if daily == True:
            self.data = fred.get_series('AAA10Y', observation_start='01/03/1983', observation_end=observation_end)
        else:
            self.data = fred.get_series('AAA10YM', observation_start='04/01/1953', observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Percent'])
    def BAA_to_10_Year(self, daily = True, observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Moody's Seasoned Baa Corporate Bond Yield Relative to Yield on 10-Year Treasury Constant Maturity (Daily or Monthly)'''
        if daily == True:
            self.data = fred.get_series('BAA10Y', observation_start='01/03/1986', observation_end=observation_end)
        else:
            self.data = fred.get_series('BAA10YM', observation_start='04/01/1953', observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Percent'])
    def AAA_minus_FFR(self, daily = True, observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Moody's Seasoned Aaa Corporate Bond Minus Federal Funds Rate (Daily or Monthly)'''
        if daily == True:
            self.data = fred.get_series('AAAFF', observation_start='01/03/1983', observation_end=observation_end)
        else:
            self.data = fred.get_series('AAAFFM', observation_start='07/01/1954', observation_end=observation_end)
        return pd.DataFrame(self.data,columns=['Percent'])


        


