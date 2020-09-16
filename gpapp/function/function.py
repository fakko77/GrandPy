import requests
from operator import itemgetter


def getList(dict):
    return list(map(itemgetter(0), dict.items()))

def getInfo(id):
    r = requests.get(
            "https://fr.wikipedia.org/w/api.php?format=json"
            "&action=query&prop=extracts&exintro&explaintext&redirects=1&pageids=" + str(id))
    results = r.json()['query']['pages'][str(id)]
    results = results['extract']
    return results
# def searchCity(city):
#     """search for the city and give  location """
#     r = requests.get("https://maps.googleapis.com"
#                      "/maps/api/geocode/json?address=" + city + "&key=AIzaSyAr9x7A9TvznnGv43D0ZFB3e3c9IIIm3cQ")
#     # print("ici")
#     results = r.json()['results']
#     # print(results)
#     location = results[0]['geometry']['location']
#     # print(results[0])
#     return location
#
#
# def getId(location):
#     lat = location['lat']
#     lng = location['lng']
#     r = requests.get(
#         "https://fr.wikipedia.org/w/api.php?action=query&list"
#         "=geosearch&gscoord=" + str(lat) + "|" + str(lng) + "&gsradius=10000&gslimit=1&format=json")
#     results = r.json()['query']['geosearch']
#     id = results[0]['pageid']
#     return id
#
