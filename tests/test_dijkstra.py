import unittest
import types
from src.grafosimple import GrafoSimple
from src.dijkstra import Dijkstra

class TestGrafoSimple(unittest.TestCase):
    def test_vacio(self):
        grafo = GrafoSimple()
        self.assertRaises(Exception,Dijkstra,grafo,0)
