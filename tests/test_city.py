from model.City import City
import requests
from function.function import getInfo
from io import BytesIO
import json

import unittest
from unittest.mock import patch







class TestCity():
    PARISCORD = {'lat': 48.856614, 'lng': 2.3522219}
    ERROR = "ERROR"
    IDPARIS = 7785129
    ville = City("Paris")
    ville_error = City("GHFDDHGO")


    def test_searchCity_return_location(self):
        assert self.ville.searchCity() == self.PARISCORD

    def test_searchCity_return_error(self):
        assert self.ville_error.searchCity() == self.ERROR


    def test_getid(self):
        ville = City("Paris")
        cord = ville.searchCity()
        id = ville.getId(cord)
        assert id == self.IDPARIS

    def test_searchCity_mock(self,monkeypatch):
        results = {'lat': 48.856614, 'lng': 2.3522219}

        def mock_get(requests):
            return results

        monkeypatch.setattr(requests, 'get', mock_get)
        assert self.ville.searchCity() == results

    def test_getId_mock(self,monkeypatch):
        results = 7785129

        def mock_get(requests):
            return results
        print(self.ville.getId(self.PARISCORD))
        monkeypatch.setattr(requests, 'get', mock_get)
        assert self.ville.getId(self.PARISCORD) == results
