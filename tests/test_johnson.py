import unittest

from src.grafosimple import GrafoSimple
from src.johnson import Johnson

class TestJohnson(unittest.TestCase):
    def test_vacio(self):
        grafo = GrafoSimple()
        self.assertRaises(Exception,Johnson,grafo)

