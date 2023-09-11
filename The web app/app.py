from flask import Flask, request, jsonify
from functools import lru_cache
from cachetools import TTLCache
import requests


app = Flask(__name__)

cache = TTLCache(ttl=1799, maxsize=1)


def get_headers():
    if "key" in cache:
        return cache["key"]

    url = "https://test.api.amadeus.com/v1/security/oauth2/token?grant_type=client_credentials"
    payload = 'grant_type=client_credentials&client_id=vbBEiaYVFLSXbtJgXUOwmJrvTn0DffGR&client_secret=JtgN8WKBP6apH5ix'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    token = response.json()["access_token"]
    cache["key"] = {"Authorization": "Bearer {}".format(token)}
    return {"Authorization": "Bearer {}".format(token)}


@app.route('/search-flight', methods=['GET'])
def search_flight():
    source = request.args.get('source')
    destination = request.args.get('destination')
    date = request.args.get('date')

    header = get_headers()
    response = requests.request("GET", f'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode={source}&destinationLocationCode={destination}&departureDate={date}&adults=1',
                                headers=header)
    flights = response.json()
    return jsonify(flights)    # Return the flight data as JSON response


if __name__ == '__main__':
    app.run(debug=True)
