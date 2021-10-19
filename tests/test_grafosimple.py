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

    def test_BA5(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("B","A",5)
        self.assertEqual(2,grafo.cantidadNodos())
        self.assertEqual(1,grafo.cantidadArcos())
        self.assertEqual(grafo.idDeNodoAlias("B"),0)
        self.assertEqual(grafo.idDeNodoAlias("A"),1)
        self.assertEqual(list(grafo.arcoDesdeNodoId(0)), [(1,5)])
        self.assertEqual(list(grafo.arcoDesdeNodoId(1)), [])

    def test_AB9BA5(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",9)
        grafo.insertarArcoConAlias("B","A",5)
        self.assertEqual(2,grafo.cantidadNodos())
        self.assertEqual(2,grafo.cantidadArcos())
        self.assertEqual(grafo.idDeNodoAlias("A"),0)
        self.assertEqual(grafo.idDeNodoAlias("B"),1)
        self.assertEqual(list(grafo.arcoDesdeNodoId(0)), [(1,9)])
        self.assertEqual(list(grafo.arcoDesdeNodoId(1)), [(0,5)])

    def test_Ax10xA20_siendo_x_objeto(self):
        grafo = GrafoSimple()
        x = object()
        grafo.insertarArcoConAlias("A",x,10)
        grafo.insertarArcoConAlias(x,"A",20)
        self.assertEqual(2,grafo.cantidadNodos())
        self.assertEqual(2,grafo.cantidadArcos())
        self.assertEqual(grafo.idDeNodoAlias("A"),0)
        self.assertEqual(grafo.idDeNodoAlias(x),1)
        self.assertEqual(list(grafo.arcoDesdeNodoId(0)), [(1,10)])
        self.assertEqual(list(grafo.arcoDesdeNodoId(1)), [(0,20)])

if __name__ == '__main__':
    unittest.main()