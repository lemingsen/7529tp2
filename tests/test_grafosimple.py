import unittest
from src.grafosimple import GrafoSimple

class TestGrafoSimple(unittest.TestCase):
    def test_vacio(self):
        grafo = GrafoSimple()
        self.assertEqual(0,grafo.cantidadNodos())
        self.assertEqual(0,grafo.cantidadArcos())

    def test_AB10_cantidad(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",10)
        self.assertEqual(2,grafo.cantidadNodos())
        self.assertEqual(1,grafo.cantidadArcos())

if __name__ == '__main__':
    unittest.main()