import requests

class City:
    """ class for create a City """
    def __init__(self, name):
        self.name = name

    def searchCity(self):
        try:
            city = self.name
            """search for the city and give  location """
            r = requests.get("https://maps.googleapis.com"
                             "/maps/api/geocode/json?address=" + city + "&key=AIzaSyAr9x7A9TvznnGv43D0ZFB3e3c9IIIm3cQ")
            results = r.json()['results']
            location = results[0]['geometry']['location']
            return location
        except IndexError:
            location = "ERROR"
            return location

    def getId(self, location):
        lat = location['lat']
        lng = location['lng']
        r = requests.get(
            "https://fr.wikipedia.org/w/api.php?action=query&list"
            "=geosearch&gscoord=" + str(lat) + "|" + str(lng) + "&gsradius=10000&gslimit=1&format=json")
        results = r.json()['query']['geosearch']
        id = results[0]['pageid']
        return id


