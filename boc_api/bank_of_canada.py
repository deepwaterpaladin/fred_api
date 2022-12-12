import json
import requests
import pandas as pd

class BOC():
    def __init__(self, url):
        self.url = url

    # Get the data from the API
    def get_data(self):
        response = requests.get(self.url)
        data = json.loads(response.text)
        df = pd.json_normalize(data["observations"])
        df.set_index("d", inplace=True)
        return df
    