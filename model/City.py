import requests
import json
import os
class City:
    """ class for create a City """

    def __init__(self, name):
        self.name = name

    def searchCity(self):
        """ search city  location"""
        key = os.getenv("key")
        try:
            city = self.name
            """search for the city and give  location """
            r = requests.get("https://maps.googleapis.com"
                             "/maps/api/geocode/json?address=" + city +
                             "&key="+key+"")
            if isinstance(r, dict):
                location = json.dumps(r)
                location = json.loads(location)
                print(type(location))
                return location
            else:
                results = r.json()['results']
                location = results[0]['geometry']['location']
                print(location, "type:", type(location))
            return location

        except IndexError:
            location = "ERROR"
            location = "ERROR"
            return location

    def getId(self, location):
        lat = location['lat']
        lng = location['lng']
        r = requests.get(
            "https://fr.wikipedia.org/w/api.php?action=query&list"
            "=geosearch&gscoord=" + str(lat) + "|" + str(lng) +
            "&gsradius=10000&gslimit=1&format=json")
        if isinstance(r, int):
            id = r
            return id
        else:
            results = r.json()['query']['geosearch']
            id = results[0]['pageid']
            print(type(id))
        return id
