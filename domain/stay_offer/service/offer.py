from typing import Tuple
from domain.stay_offer.models.offer import StayOffer

def calculate_stay_offer(start: str, end: str, latitude: str, longitude: str, airbnb_id: str) -> Tuple[StayOffer, int, str]:    
    offer = StayOffer(start=start, end=end, latitude=latitude, longitude=longitude, airbnb_id=airbnb_id)
    try:
        err = offer.validate()
        if err is not None:
            return None, 400, err 

        offer.calculate_price()
        return offer, 200, None
    except:
        raise Exception("internal server error")