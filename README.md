# Introduction

## Getting Started

1. Install dependencies -> `pip install requirements.txt`
1. create `.env` file
1. add `API_KEY` constant to `.env` file & add API key

## Using the Package

1. files in the `src` directory are up to date
1. `commodities.py` features:
    - `Commodity()` class is the main class
    - `Metals()`, `Agriculture()`, `Energy()`, & `Livestock()` are subclasses of `Commodity()`
        - `Metals()`: `IronOre()`, `Copper()`, `Aluminum()`, `Lead()`, `Zinc()`, `Nickel()`, `Tin()`, & `Uranium()`
        - `Agriculture()`: `Corn()`, `Soybeans()`, `Wheat()`, `Cotton()`, `Barley()`, `Coffee()`, `Cocoa()`, `Bananas()`, & `OliveOil()`
        - `Energy()`: `Natural Gas()`, & `Oil()`
        - `Livestock()`: `Shrimp()`, `Swine()`, `Beef()`,  `Shellfish()`, `Lamb()`, `Poultry()`, & `Fish()`
    - Data can be accessed via `x_week/month_price()` method with x being the number of weeks/months
       - returns a pandas dataframe
    - Plot the data via the `plot()` method
       - returns a `plotly` chart
1. As files in the `src` directory are updated, the `README.md` file will be updated to reflect the changes (eventually this will be `__init__.py` file being updated once this is a proper package)

## About FRED API

- The Federal Reserve Economic Data (FRED) API is a web service for obtaining economic data from the Federal Reserve Bank of St. Louis.  
- The FRED API is a RESTful web service that returns data in JSON, XML, or CSV format. The FRED API is free to use.
- [FRED API Documentation](https://fred.stlouisfed.org/docs/api/fred/)

## TODO

1. Refactor following files in the style of `class Oil` in `commodities.py`:
    - [ ] `bonds.py`
    - [ ] `business_expectations.py`
    - [X] `commodities.py`
    - [ ] `consumer_credit.py`
    - [ ] `delinquency.py`
    - [ ] `exchange_rate.py`
    - [ ] `housing.py`
    - [ ] `monetary_policy.py`
    - [ ] `producer_prices.py`
    - [ ] `stocks.py`
    - [ ] `uncertainty.py`
    - [ ] `unemployment.py`
1. Add more data to the database
