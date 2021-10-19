import unittest

from src.grafosimple import GrafoSimple
from src.bellmanford import BellmanFordConCeroAgregado

class TestBellmanFordCero(unittest.TestCase):
    def test_vacio(self):
        grafo = GrafoSimple()
        self.assertRaises(Exception,BellmanFordConCeroAgregado,grafo)

    def test_AB5(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",5)
        self.assertEqual(BellmanFordConCeroAgregado(grafo).distancias, [0, 0])
