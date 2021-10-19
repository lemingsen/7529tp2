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



if __name__ == '__main__':
    unittest.main()