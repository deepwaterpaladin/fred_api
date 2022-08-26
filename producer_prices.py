import pandas as pd
from datetime import date
from fred_api_key import fred

class PPI():
    def __init__(self) -> None:
        pass
    def all_commodities(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Producer Price Index by Commodity: All Commodities'''
        self.data = fred.get_series('PPIACO', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Index 1980=100'])
    def total_manufacturing(self, observation_start='01/01/2000', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        ''' Producer Price Index by Industry: Total Manufacturing Industries'''
        self.data = fred.get_series('PCUOMFGOMFG', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Index 1984=100'])

print(PPI().all_commodities().tail(12))