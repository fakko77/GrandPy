from model.City import City

def test_searchCity():
    ville = City("Paris")
    assert ville.searchCity() == {'lat': 48.856614, 'lng': 2.3522219}

def test_searchCity1():
    ville = City("GHFDDHGO")
    assert ville.searchCity() == "ERROR"


def test_getid():
    ville = City("Paris")
    cord = ville.searchCity()
    id = ville.getId(cord)
    assert id == 7785129
