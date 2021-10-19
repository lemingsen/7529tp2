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

    def test_AB6BA7AC1CA2(self):
        rutaArchivo = self.pathArchivo("entradas/test_AB6BA7AC1CA2.txt")
        grafo = Lector(rutaArchivo).grafo
        self.assertEqual( list(grafo.arcoDesdeNodoId(0)), [ (1,6), (2,1) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(1)), [ (0,7) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(2)), [ (0,2)])

    def test_ejtp2_pos(self):
        """Grafo H del TP2 (todos positivos)"""
        rutaArchivo = self.pathArchivo("entradas/test_ejtp2_pos.txt")
        grafo = Lector(rutaArchivo).grafo
        self.assertEqual( list(grafo.arcoDesdeNodoId(0)), [ (1,14), (2, 1) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(1)), [ (2, 1), (3,13)  ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(2)), [ (4,17) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(3)), [ (1, 0) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(4)), [ (0, 8), (2, 0), (3,13) ])

    def test_cormen_pos(self):
        """Ejemplo tomado de Cormen et al. «Intorduction to Algorithms», 3ª ed.
        Corresponde al grafo obtenido luego de aplicar Bellman-Ford."""
        rutaArchivo = self.pathArchivo("entradas/test_cormen.txt")
        grafo = Lector(rutaArchivo).grafo
        self.assertEqual( list(grafo.arcoDesdeNodoId(0)), [ (1,4), (2,13), (4,0) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(1)), [ (3,0), (4,10) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(2)), [ (1,0) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(3)), [ (0,2), (2,0) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(4)), [ (3,2) ])

    def test_ciclo_positivo(self):
        rutaArchivo = self.pathArchivo("entradas/test_ciclo_positivo.txt")
        grafo = Lector(rutaArchivo).grafo
        self.assertEqual( list(grafo.arcoDesdeNodoId(0)), [ (1, -5) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(1)), [ (2,-10) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(2)), [ (0, 20) ])

    def test_4nodos_con_negativos(self):
        rutaArchivo = self.pathArchivo("entradas/test_4nodos_con_negativos.txt")
        grafo = Lector(rutaArchivo).grafo
        self.assertEqual( list(grafo.arcoDesdeNodoId(0)), [ (1,-2), (3,-1) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(1)), [ (2,5) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(2)), [ (3,-2) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(3)), [ (1-3,) ])

    def test_5nodos_con_negativos(self):
        rutaArchivo = self.pathArchivo("entradas/test_5nodos_con_negativos.txt")
        grafo = Lector(rutaArchivo).grafo
        self.assertEqual( list(grafo.arcoDesdeNodoId(0)), [ (1,6) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(1)), [ (2,-2), (4,-1) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(2)), [ (0,0), (3,5) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(3)), [ (4,-2) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(4)), [ (2,-3) ])

    def test_cormen(self):
        """Ejemplo tomado de Cormen et al. «Intorduction to Algorithms», 3ª ed."""
        rutaArchivo = self.pathArchivo("entradas/test_cormen.txt")
        grafo = Lector(rutaArchivo).grafo
        self.assertEqual( list(grafo.arcoDesdeNodoId(0)), [ (1,3), (2,8), (4,-4) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(1)), [ (3,1), (4,7) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(2)), [ (1,4) ])
        self.assertEqual( list(grafo.arcoDesdeNodoId(3)), [ (0,2), (2,-5)])
        self.assertEqual( list(grafo.arcoDesdeNodoId(4)), [ (3,6) ])

if __name__ == '__main__':
    unittest.main()