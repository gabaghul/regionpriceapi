import pandas as pd

# constant_price = None

def load_constant_price():
    constant_price = pd.read_csv('data/constant_price.csv', delimiter=",")
    return constant_price 