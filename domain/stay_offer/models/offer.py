from datetime import datetime
import random

class StayOffer:
    def __init__(self, start: str, end: str, latitude: str, longitude: str, total_guests: str):
        self.start = start
        self.end = end
        self.latitude = latitude
        self.longitude = longitude
        self.total_guests = total_guests
        self.price = 0

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

        if self.total_guests is None or self.total_guests == "":
            message = "total guests is required"

        try:
            int(self.total_guests)
        except ValueError:
            message = "total guests must be numeric"

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
        start = datetime.strptime(self.start, "%Y-%m-%d")
        end = datetime.strptime(self.end, "%Y-%m-%d")
        day_price = random.uniform(20, 200)
        date_diff_in_days = (end - start).days
        self.price = round(day_price * date_diff_in_days * int(self.total_guests), 2)

    def to_dict(self) -> dict:
        return {
            'start': self.start,
            'end': self.end,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'total_guests': self.total_guests,
            'price': self.price
        }