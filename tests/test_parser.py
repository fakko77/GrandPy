from variables import PARSER
from model.ParserKiller import Killer


def test_parser():
    msg = "a abord absolument afin ah ai aie ailleurs ainsi ait allaient allo allons"
    kil = Killer(msg)
    assert kil.parser(PARSER) == []


def test_parser1():
    msg = "a abord absolument afin ah ai morgan aie ailleurs ainsi ait allaient allo allons"
    kil = Killer(msg)
    assert kil.parser(PARSER) == ["morgan"]