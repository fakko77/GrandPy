from model.City import City
from variables import MOCK_RESPONSE_searchCity, MOCK_RESPONSE_getId
import requests
import responses


class TestCity():
    PARISCORD = {'lat': 48.856614, 'lng': 2.3522219}
    ERROR = "ERROR"
    IDPARIS = 7785129
    ville = City("Paris")
    ville_error = City("GHFDDHGO")

    @responses.activate
    def test_searchCity_mock(self,monkeypatch):
        resultat = {'lat': 48.856614, 'lng': 2.3522219}
        responses.add(responses.GET, 'http://mock_test.com',
                      json=MOCK_RESPONSE_searchCity)
        resp = requests.get('http://mock_test.com')
        def mock_get(requests):
            return resp
        monkeypatch.setattr(requests, 'get', mock_get)
        assert self.ville.searchCity() == resultat

    @responses.activate
    def test_getId_mock(self,monkeypatch):
        resultat = 7785129
        responses.add(responses.GET, 'http://mock_test.com',
                      json=MOCK_RESPONSE_getId)
        resp = requests.get('http://mock_test.com')

        def mock_get(requests):
            return resp
        monkeypatch.setattr(requests, 'get', mock_get)
        assert self.ville.getId(self.PARISCORD) == resultat

    def test_searchCity_return_location(self):
        assert self.ville.searchCity() == self.PARISCORD

    def test_searchCity_return_error(self):
        assert self.ville_error.searchCity() == self.ERROR

    def test_getid(self):
        ville = City("Paris")
        cord = ville.searchCity()
        id = ville.getId(cord)
        assert id == self.IDPARIS