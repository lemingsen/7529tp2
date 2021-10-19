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
