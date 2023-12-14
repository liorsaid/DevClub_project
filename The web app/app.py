import requests
from functools import lru_cache
from cachetools import TTLCache
import os
from flask_cors import CORS, cross_origin
from flask import Flask, send_from_directory, request, jsonify

ROOT_FOLDER = 'Users\\לי אור\\Desktop\\FlightApp\\my-app\\src'
app = Flask(__name__, static_folder=os.path.join(ROOT_FOLDER, 'static'))
cors = CORS(app) #allows cors for our frontend

cache = TTLCache(ttl=1799, maxsize=1)

# Given function to retrieve access token
def get_headers():
    if "key" in cache:
        return cache["key"]

    url = "https://test.api.amadeus.com/v1/security/oauth2/token?grant_type=client_credentials"
    payload = 'grant_type=client_credentials&client_id=ku5SQ4SYas3s8phK0ru7MqA7UrckAMKt&client_secret=gkfuh5h4LRw4iG5b'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    token = response.json()["access_token"]
    cache["key"] = {"Authorization": "Bearer {}".format(token)}
    return {"Authorization": "Bearer {}".format(token)}

# Function to perform API request using obtained headers
def make_api_request(dest, loc, date):
    headers = get_headers()
    response = requests.request(
        "GET",
        f'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode={loc}&destinationLocationCode={dest}&departureDate={date}&adults=1',
        headers=headers
    )
    flights = response.json()
    return flights['data'][0]

@app.route('/get_flight_offers', methods=['GET'])
def get_flight_offers():
    loc = request.args.get('location')
    dest = request.args.get('destination')
    date = request.args.get('date')

    api_response = make_api_request(dest, loc, date)
    return jsonify(api_response)

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>', methods=["GET"])
def files(path):
    return send_from_directory(ROOT_FOLDER, path)

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
