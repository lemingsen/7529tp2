import unittest
import types
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

    def test_AB10_adyctentes(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",10)
        self.assertEqual(list(grafo.arcoDesdeNodoId(0)), [(1,10)])
        self.assertEqual(list(grafo.arcoDesdeNodoId(1)), [])
        self.assertRaises(Exception, grafo.arcoDesdeNodoId, 2)
        self.assertRaises(Exception, grafo.arcoDesdeNodoId, -1)

    def test_arcoDesdeNodoId_es_generador(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",10)
        adyacentes = grafo.arcoDesdeNodoId(0)
        self.assertTrue(isinstance(adyacentes, types.GeneratorType))

if __name__ == '__main__':
    unittest.main()