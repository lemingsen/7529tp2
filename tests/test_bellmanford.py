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

    def test_ciclo_positivo(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",-5)
        grafo.insertarArcoConAlias("B","C",-10)
        grafo.insertarArcoConAlias("C","A",20)
        self.assertEqual(BellmanFordConCeroAgregado(grafo).distancias, [0, -5, -15])

    def test_2rondas(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",-2)
        grafo.insertarArcoConAlias("C","D",-2)
        grafo.insertarArcoConAlias("A","D",-1)
        grafo.insertarArcoConAlias("B","C",5)
        grafo.insertarArcoConAlias("D","B",-3)
        distancias = BellmanFordConCeroAgregado(grafo).distancias
        self.assertEqual(distancias[grafo.idDeNodoAlias("A")], 0)
        self.assertEqual(distancias[grafo.idDeNodoAlias("B")], -5)
        self.assertEqual(distancias[grafo.idDeNodoAlias("C")], 0)
        self.assertEqual(distancias[grafo.idDeNodoAlias("D")], -2)