from datetime import datetime
import random
import pandas as pd
from domain.driver.price_per_month import prices_per_month
from domain.driver.constant_price import load_constant_price

class StayOffer:
    def __init__(self, start: str, end: str, latitude: str, longitude: str, airbnb_id: str):
        self.start = start
        self.end = end
        self.latitude = latitude
        self.longitude = longitude
        self.airbnb_id = airbnb_id

    def validate(self) -> str:
        message = None
        if self.latitude is None:
            message = "latitude is required"

        try:
            float(self.latitude)
        except ValueError:
            message = "latitude must be numeric"

        if self.longitude is None:
            message = "longitude is required"

        try:
            float(self.longitude)
        except ValueError:
            message = "longitude must be numeric"

        if self.start is None or self.start == "":
            message = "start date is required"

        if self.end is None or self.end == "":
            message = "end date is required"

        if self.airbnb_id is None or self.airbnb_id == "":
            message = "airbnb id is required"

        try:
            start = datetime.strptime(self.start, "%Y-%m-%d")
            end = datetime.strptime(self.end, "%Y-%m-%d")
        except:
            message = "must use timestamp yyyy-mm-dd"

        if start.date() < datetime.now().date():
            message = "start date must be greater or equals than today"

        if end.date() <= start.date():
            message = "end date must be greater than start date"
        
        return message

    def calculate_price(self):
        self.price = self._get_fee_for_start_date() + self._get_constant_fee_for_airbnb()

    def _get_fee_for_start_date(self):
        DATE_FORMAT = "%Y-%m-%d"
        start = datetime.strptime(self.start, DATE_FORMAT)
        first_date = start.replace(day=1).strftime(DATE_FORMAT)

        price = prices_per_month[first_date]
        return price / 1e8 +3


    def to_dict(self) -> dict:
        return {
            'start': self.start,
            'end': self.end,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'airbnb_id': self.airbnb_id,
            'price': self.price
        }
    
    def _get_constant_fee_for_airbnb(self):
        constant_price = load_constant_price()
        id = int(self.airbnb_id)

        fee = constant_price[constant_price['id'] == id].iloc[0]['constant_price']
        
        return fee 