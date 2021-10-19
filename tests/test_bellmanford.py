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

    def testAB_menos2(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",-2)
        self.assertEqual(BellmanFordConCeroAgregado(grafo).distancias, [0, -2])
