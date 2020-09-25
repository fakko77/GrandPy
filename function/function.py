import requests
from operator import itemgetter


def get_list(dict_test):
    return list(map(itemgetter(0), dict_test.items()))


def get_info(id_page):
    r = requests.get(
            "https://fr.wikipedia.org/w/api.php?format=json"
            "&action=query&prop=extracts&exintro&explaintext&redirects=1&pageids=" + str(id_page))
    results = r.json()['query']['pages'][str(id_page)]
    results = results['extract']
    return results
