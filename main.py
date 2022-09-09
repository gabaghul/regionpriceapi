from domain.driver.price_per_month import load_prices_per_month
from domain.driver.constant_price import load_constant_price
import server.api as api


if __name__ == '__main__':
    load_prices_per_month()
    api.start()