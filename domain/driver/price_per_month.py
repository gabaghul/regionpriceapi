import pandas as pd

prices_per_month = {}

def load_prices_per_month():
    data = pd.read_csv('data/price_per_month.csv', delimiter=",")

    for _, row in data.iterrows():
        prices_per_month[row['ds']] = row['yhat']

