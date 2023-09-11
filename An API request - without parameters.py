from functools import lru_cache
from cachetools import TTLCache
import requests
from pymongo import MongoClient

# client = MongoClient('mongodb+srv://AmitKartun:AmitKartun15@cluster0.j8py5wt.mongodb.net/', 27017)
# db = client["FlightsDB"]
# collection = db["Flights"]

cache = TTLCache(ttl=1799, maxsize=1)


# given
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


header = get_headers()
response = requests.request("GET", 'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=SYD&destinationLocationCode=BKK&departureDate=2023-10-10&adults=1',
                            headers=header)
flights = response.json()
print(flights['data'][0])



# collection.insert_one(flights['data'][0])
