from model.City import City

ville = City("Paris")


def test_searchCity():
    assert ville.searchCity() == {'lat': 48.856614, 'lng': 2.3522219}


def test_getid():
    cord = ville.searchCity()
    id = ville.getId(cord)
    assert id == 7785129
