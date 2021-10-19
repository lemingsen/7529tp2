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

    def test_2rondasb(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B", 6)
        grafo.insertarArcoConAlias("B","C",-2)
        grafo.insertarArcoConAlias("C","A", 0)
        grafo.insertarArcoConAlias("D","E",-2)
        grafo.insertarArcoConAlias("B","E",-1)
        grafo.insertarArcoConAlias("C","D", 5)
        grafo.insertarArcoConAlias("E","C",-3)
        distancias = BellmanFordConCeroAgregado(grafo).distancias
        self.assertEqual(distancias[grafo.idDeNodoAlias("A")], -5)
        self.assertEqual(distancias[grafo.idDeNodoAlias("B")],  0)
        self.assertEqual(distancias[grafo.idDeNodoAlias("C")], -5)
        self.assertEqual(distancias[grafo.idDeNodoAlias("D")],  0)
        self.assertEqual(distancias[grafo.idDeNodoAlias("E")], -2)

    def test_cormen(self):
        """Ejemplo tomado de Cormen et al. «Intorduction to Algorithms», 3ª ed."""
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("1","2", 3)
        grafo.insertarArcoConAlias("1","3", 8)
        grafo.insertarArcoConAlias("2","4", 1)
        grafo.insertarArcoConAlias("2","5", 7)
        grafo.insertarArcoConAlias("1","5",-4)
        grafo.insertarArcoConAlias("3","2", 4)
        grafo.insertarArcoConAlias("4","1", 2)
        grafo.insertarArcoConAlias("4","3",-5)
        grafo.insertarArcoConAlias("5","4", 4)

        distancias = BellmanFordConCeroAgregado(grafo).distancias

        self.assertEqual(distancias[grafo.idDeNodoAlias("1")],  0)
        self.assertEqual(distancias[grafo.idDeNodoAlias("2")], -1)
        self.assertEqual(distancias[grafo.idDeNodoAlias("3")], -5)
        self.assertEqual(distancias[grafo.idDeNodoAlias("4")],  0)
        self.assertEqual(distancias[grafo.idDeNodoAlias("5")], -4)

    def test_tp2(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("1","2", 12)
        grafo.insertarArcoConAlias("1","3", -3)
        grafo.insertarArcoConAlias("2","3", -1)
        grafo.insertarArcoConAlias("2","4", 15)
        grafo.insertarArcoConAlias("3","5", 21)
        grafo.insertarArcoConAlias("4","2", -2)
        grafo.insertarArcoConAlias("5","1",  8)
        grafo.insertarArcoConAlias("5","3", -4)
        grafo.insertarArcoConAlias("5","4", 13)

        distancias = BellmanFordConCeroAgregado(grafo).distancias

        self.assertEqual(distancias[grafo.idDeNodoAlias("1")],  0)
        self.assertEqual(distancias[grafo.idDeNodoAlias("2")], -2)
        self.assertEqual(distancias[grafo.idDeNodoAlias("3")], -4)
        self.assertEqual(distancias[grafo.idDeNodoAlias("4")],  0)
        self.assertEqual(distancias[grafo.idDeNodoAlias("5")],  0)
