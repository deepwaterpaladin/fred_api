import pandas as pd
from datetime import date
from src.fred_api_key import fred

class BusinessExpectations():
    def __init__(self) -> None:
        pass
    def sales_revenue_growth(self, observation_start='01/01/2016', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Business Expectations: Sales Revenue Growth'''
        self.data = fred.get_series('ATLSBUSRGEP', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Percent'])
    def employment_growth(self, observation_start='01/01/2016', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Business Expectations: Employment Growth'''
        self.data = fred.get_series('ATLSBUEGEP', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Percent'])

class BusinessUncertainty():
    def __init__(self) -> None:
        pass
    def sales_revenue_growth(self, observation_start='01/01/2016', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Business Uncertainty: Sales Revenue Growth'''
        self.data = fred.get_series('ATLSBUSRGUP', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Percent'])
    def employment_growth(self, observation_start='01/01/2016', observation_end=date.today().strftime("%m/%d/%Y"))->pd.DataFrame:
        '''Business Uncertainty: Employment Growth'''
        self.data = fred.get_series('ATLSBUEGUP', observation_start = observation_start, observation_end=observation_end)
        return pd.DataFrame(self.data, columns=['Percent'])

x = BusinessUncertainty().sales_revenue_growth().tail(12)
y = BusinessUncertainty().employment_growth().tail(12)
print(x, y)