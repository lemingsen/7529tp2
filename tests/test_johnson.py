import math
import unittest

from src.grafosimple import GrafoSimple
from src.johnson import Johnson

class TestJohnson(unittest.TestCase):
    def test_vacio(self):
        grafo = GrafoSimple()
        self.assertRaises(Exception,Johnson,grafo)

    def test_AB0BA0(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",0)
        grafo.insertarArcoConAlias("B","A",0)
        johnson = Johnson(grafo)
        self.assertEqual(len(johnson.matriz), 2)
        self.assertEqual(len(johnson.matriz[0]), 2)
        self.assertEqual(len(johnson.matriz[1]), 2)
        self.assertEqual(johnson.matriz[0], [0,0])
        self.assertEqual(johnson.matriz[1], [0,0])

    def test_AB11(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",11)
        johnson = Johnson(grafo)
        self.assertEqual(len(johnson.matriz), 2)
        self.assertEqual(johnson.matriz[0], [0,11])
        self.assertEqual(johnson.matriz[1], [math.inf,0])

    def test_AB6BA7AC1CA2(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",6)
        grafo.insertarArcoConAlias("B","A",7)
        grafo.insertarArcoConAlias("A","C",1)
        grafo.insertarArcoConAlias("C","A",2)
        johnson = Johnson(grafo)
        self.assertEqual(len(johnson.matriz), 3)
        self.assertEqual(johnson.matriz[0], [0,6,1])
        self.assertEqual(johnson.matriz[1], [7,0,8])
        self.assertEqual(johnson.matriz[2], [2,8,0])

    def test_ejtp2_pos(self):
        """Grafo H del TP2 (todos positivos)"""
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("1","2",14)
        grafo.insertarArcoConAlias("1","3",1)
        grafo.insertarArcoConAlias("2","3",1)
        grafo.insertarArcoConAlias("2","4",13)
        grafo.insertarArcoConAlias("3","5",17)
        grafo.insertarArcoConAlias("4","2",0)
        grafo.insertarArcoConAlias("5","1",8)
        grafo.insertarArcoConAlias("5","3",0)
        grafo.insertarArcoConAlias("5","4",13)

        johnson = Johnson(grafo)

        self.assertEqual(johnson.matriz[grafo.idDeNodoAlias("1")], [ 0,14,1,27,18])
        self.assertEqual(johnson.matriz[grafo.idDeNodoAlias("2")], [26, 0,1,13,18])
        self.assertEqual(johnson.matriz[grafo.idDeNodoAlias("3")], [25,30,0,30,17])
        self.assertEqual(johnson.matriz[grafo.idDeNodoAlias("4")], [26, 0,1, 0,18])
        self.assertEqual(johnson.matriz[grafo.idDeNodoAlias("5")], [ 8,13,0,13, 0])

    def test_cormen(self):
        """Ejemplo tomado de Cormen et al. «Intorduction to Algorithms», 3ª ed.
        Corresponde al grafo obtenido luego de aplicar Bellman-Ford."""
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("1","2",  4)
        grafo.insertarArcoConAlias("1","3", 13)
        grafo.insertarArcoConAlias("2","4",  0)
        grafo.insertarArcoConAlias("2","5", 10)
        grafo.insertarArcoConAlias("1","5",  0)
        grafo.insertarArcoConAlias("3","2",  0)
        grafo.insertarArcoConAlias("4","1",  2)
        grafo.insertarArcoConAlias("4","3",  0)
        grafo.insertarArcoConAlias("5","4",  2)

        johnson = Johnson(grafo)
        self.assertEqual(johnson.matriz[grafo.idDeNodoAlias("1")], [0,2,2,2,0])
        self.assertEqual(johnson.matriz[grafo.idDeNodoAlias("2")], [2,0,0,0,2])
        self.assertEqual(johnson.matriz[grafo.idDeNodoAlias("3")], [2,0,0,0,2])
        self.assertEqual(johnson.matriz[grafo.idDeNodoAlias("4")], [2,0,0,0,2])
        self.assertEqual(johnson.matriz[grafo.idDeNodoAlias("5")], [4,2,2,2,0])
