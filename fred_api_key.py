import os
from fredapi import Fred
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.env('API_KEY')

fred = Fred(api_key=API_KEY)