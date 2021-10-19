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

    def test_AB10_nodos(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",10)
        self.assertEqual(grafo.idDeNodoAlias("A"),0)
        self.assertEqual(grafo.idDeNodoAlias("B"),1)

    def test_idDeNodoAliasNoExistente(self):
        grafo = GrafoSimple()
        self.assertRaises(Exception,grafo.idDeNodoAlias,"A")
        self.assertEqual(grafo.idDeNodoAlias("A",crear=True),0)

if __name__ == '__main__':
    unittest.main()