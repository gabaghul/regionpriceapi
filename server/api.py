from crypt import methods
from datetime import datetime
import json
import logging
from urllib.parse import unquote
import uuid
from flask import Flask, request, Response

import domain.stay_offer.service.offer as service

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask!!"

@app.route("/stayoffer/regionprice", methods=["GET"])
def region_price():
    if request.method == "GET":
        _logger = logging.getLogger()
        _logger.setLevel(logging.DEBUG)
        now = datetime.now()
        request_id = str(uuid.uuid4())
        args = request.args

        # removing urlencode
        start = unquote(args.get('start'))
        end = unquote(args.get('end'))
        latitude = unquote(args.get('latitude'))
        longitude = unquote(args.get('longitude'))
        total_guests = unquote(args.get('totalGuests'))
        offer, status_code, message = service.calculate_stay_offer(
            start=start,
            end=end,
            latitude=latitude,
            longitude=longitude,
            total_guests=total_guests
        )
        if status_code == 200:
            return Response(response=json.dumps({
                'body' : offer.to_dict(),
                'message': "everything went fine!",
            }), status=status_code, mimetype="application/json")
        elif status_code == 400:
            _logger.error(f'''[
                request_id: {request_id}, 
                now: {now}, 
                start: {start}, 
                end: {end}, 
                latitude: {latitude}, 
                longitude: {longitude}, 
                total_guests:{total_guests}
            ] bad request: {message}''')
            return Response(response=json.dumps({
                'message': f'bad request: {message}'
            }), status=status_code, mimetype="application/json")
        else:
            _logger.error(f'''[
                request_id: {request_id}, 
                now: {now}, 
                start: {start}, 
                end: {end}, 
                latitude: {latitude}, 
                longitude: {longitude}, 
                total_guests:{total_guests}
            ] internal server error: {message}''')
            return Response(response=json.dumps({
                'message': f'internal server error'
            }), status=status_code, mimetype="application/json")

def start():
    app.run(host='0.0.0.0',port=5000)