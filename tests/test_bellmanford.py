import unittest

from src.grafosimple import GrafoSimple
from src.bellmanford import BellmanFordConCeroAgregado

class TestBellmanFordCero(unittest.TestCase):
    def test_vacio(self):
        grafo = GrafoSimple()
        self.assertRaises(Exception,BellmanFordConCeroAgregado,grafo)
