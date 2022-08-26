import yfinance as yf
import pandas as pd
from datetime import date

class Stock():
    def __init__(self, ticker) -> None:
        self.ticker = yf.Ticker(ticker)
    def market_return(self, period='2y')->pd.DataFrame:
        self.df = pd.DataFrame({"Open":self.ticker.history(period=period)["Open"],"Close":self.ticker.history(period=period)["Close"],"Volume":self.ticker.history(period=period)["Volume"],"Change":round(self.ticker.history(period=period)["Close"]-self.ticker.history(period=period)["Open"],3)})
        return self.df
