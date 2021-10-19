import os
import unittest

from src.lector import Lector

class TestLector(unittest.TestCase):
    def pathArchivo(self, rutaRelativa):
        return os.path.join(os.path.dirname(__file__), rutaRelativa)

    def test_inexistente(self):
        rutaArchivo = self.pathArchivo("entradas/nombre_de_archivo_inexistente.txt")
        self.assertRaises(Exception,Lector,rutaArchivo)

    def test_vacio(self):
        rutaArchivo = self.pathArchivo("entradas/archivo_vacio.txt")
        grafo = Lector(rutaArchivo).grafo
        self.assertEqual(0,grafo.cantidadNodos())
        self.assertEqual(0,grafo.cantidadArcos())
        self.assertEqual(0,len(list(grafo.arcos())))

    def test_AB10(self):
        rutaArchivo = self.pathArchivo("entradas/test_AB10.txt")
        grafo = Lector(rutaArchivo).grafo

        self.assertEqual(2,grafo.cantidadNodos())
        self.assertEqual(1,grafo.cantidadArcos())
        self.assertEqual(1,len(list(grafo.arcos())))
        self.assertEqual(grafo.idDeNodoAlias("A"),0)
        self.assertEqual(grafo.idDeNodoAlias("B"),1)
        self.assertEqual(list(grafo.arcos()),[(0,1,10)])

    def test_BA5_sin_retorno(self):
        rutaArchivo = self.pathArchivo("entradas/test_BA5_sin_retorno.txt")
        grafo = Lector(rutaArchivo).grafo

        self.assertEqual(2,grafo.cantidadNodos())
        self.assertEqual(1,grafo.cantidadArcos())
        self.assertEqual(1,len(list(grafo.arcos())))
        self.assertEqual(grafo.idDeNodoAlias("B"),0)
        self.assertEqual(grafo.idDeNodoAlias("A"),1)
        self.assertEqual(list(grafo.arcos()),[(0,1,5)])

    def test_BA_menos5(self):
        rutaArchivo = self.pathArchivo("entradas/test_BA_menos5.txt")
        grafo = Lector(rutaArchivo).grafo

        self.assertEqual(grafo.idDeNodoAlias("B"),0)
        self.assertEqual(grafo.idDeNodoAlias("A"),1)
        self.assertEqual(list(grafo.arcos()),[(0,1,-5)])

    def test_XY8YX9(self):
        rutaArchivo = self.pathArchivo("entradas/test_XY8YX9.txt")
        grafo = Lector(rutaArchivo).grafo

        self.assertEqual(grafo.idDeNodoAlias("X"),0)
        self.assertEqual(grafo.idDeNodoAlias("Y"),1)
        self.assertEqual(list(grafo.arcos()),[(0,1,8), (1,0,9)])

    def test_XY8YX9_espaciado(self):
        rutaArchivo = self.pathArchivo("entradas/test_XY8YX9_espaciado.txt")
        grafo = Lector(rutaArchivo).grafo

        self.assertEqual(grafo.idDeNodoAlias("X"),0)
        self.assertEqual(grafo.idDeNodoAlias("Y"),1)
        self.assertEqual(list(grafo.arcos()),[(0,1,8), (1,0,9)])

    def test_3arcos(self):
        rutaArchivo = self.pathArchivo("entradas/test_3arcos.txt")
        grafo = Lector(rutaArchivo).grafo
        self.assertEqual(4,grafo.cantidadNodos())
        self.assertEqual(3,grafo.cantidadArcos())
        self.assertEqual(grafo.idDeNodoAlias("A"),0)
        self.assertEqual(grafo.idDeNodoAlias("B"),1)
        self.assertEqual(grafo.idDeNodoAlias("D"),2)
        self.assertEqual(grafo.idDeNodoAlias("C"),3)
        self.assertEqual(list(grafo.arcos()),[(0,1,54), (0,3,-3),(1,2,8)])

    def test_nombre_largos(self):
        rutaArchivo = self.pathArchivo("entradas/test_nombre_largos.txt")
        grafo = Lector(rutaArchivo).grafo
        self.assertEqual(6,grafo.cantidadNodos())
        self.assertEqual(3,grafo.cantidadArcos())
        self.assertEqual(grafo.idDeNodoAlias("AB"),0)
        self.assertEqual(grafo.idDeNodoAlias("CD"),1)
        self.assertEqual(grafo.idDeNodoAlias("HOLA"),2)
        self.assertEqual(grafo.idDeNodoAlias("MIGUEL"),3)
        self.assertEqual(grafo.idDeNodoAlias("Estaba en la"),4)
        self.assertEqual(grafo.idDeNodoAlias("florería"),5)
        self.assertEqual(list(grafo.arcos()),[(0,1,-3), (2,3,91),(4,5,420)])

    def test_numeros(self):
        rutaArchivo = self.pathArchivo("entradas/test_numeros.txt")
        grafo = Lector(rutaArchivo).grafo
        self.assertEqual(4,grafo.cantidadNodos())
        self.assertEqual(3,grafo.cantidadArcos())
        self.assertEqual(grafo.idDeNodoAlias("A"),0)
        self.assertEqual(grafo.idDeNodoAlias("4"),1)
        self.assertEqual(grafo.idDeNodoAlias("Z"),2)
        self.assertEqual(grafo.idDeNodoAlias("CHAU"),3)
        self.assertEqual(list(grafo.arcos()),[(0,1,-1), (1,2,-2),(3,2,-3)])

if __name__ == '__main__':
    unittest.main()