from model.City import City
from variables import MOCK_RESPONSE_searchCity, MOCK_RESPONSE_getId
import requests
import responses
from config import KEY


class TestCity:
    PARIS_CORD = {'lat': 48.856614, 'lng': 2.3522219}
    ERROR = "ERROR"
    ID_PARIS = 7785129
    ville = City("Paris", KEY)
    ville_error = City("GHFDDHGO", KEY)

    @responses.activate
    def test_search_city_mock(self, monkeypatch):
        result = {'lat': 48.856614, 'lng': 2.3522219}
        responses.add(responses.GET, 'http://mock_test.com',
                      json=MOCK_RESPONSE_searchCity)
        result_mock = requests.get('http://mock_test.com')

        def mock_get(requests):
            return result_mock

        monkeypatch.setattr(requests, 'get', mock_get)
        assert self.ville.search_city() == result

    @responses.activate
    def test_get_Id_mock(self, monkeypatch):
        result = 7785129
        responses.add(responses.GET, 'http://mock_test.com',
                      json=MOCK_RESPONSE_getId)
        result_mock = requests.get('http://mock_test.com')

        def mock_get(requests):
            return result_mock

        monkeypatch.setattr(requests, 'get', mock_get)
        assert self.ville.get_id(self.PARIS_CORD) == result

    def test_search_city_return_location(self):
        assert self.ville.search_city() == self.PARIS_CORD

    def test_search_city_return_error(self):
        assert self.ville_error.search_city() == self.ERROR

    def test_get_id(self):
        ville = City("Paris", KEY)
        cord = ville.search_city()
        id_result = ville.get_id(cord)
        assert id_result == self.ID_PARIS
