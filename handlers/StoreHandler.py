import pandas as pd


class StoreHandler:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data = pd.DataFrame()
        return cls._instance

    def get_dataframe(self):
        return self.data

    def update_dataframe(self, new_data):
        self.data = pd.concat([self.data, new_data])

    def __del__(self):
        self.data.to_csv("data/test.csv", index=False)
