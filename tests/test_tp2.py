import io
import os
import subprocess
import sys
import unittest

class TestTP2(unittest.TestCase):
    def pathArchivo(self, rutaRelativa):
        return os.path.join(os.path.dirname(__file__), rutaRelativa)

    def setUp(self):
        self._python = "python"

    def ejecutar(self,argumentos):
        args = [sys.executable, self.pathArchivo("../src/tp2.py"),*argumentos]
        with subprocess.Popen(args,stdout=subprocess.PIPE,stderr=None,stdin=None,shell=False) as proc:
            yield proc.stdout.readline().decode('windows-1252')

    def test_sin_argumentos(self):
        out = self.ejecutar([])

        self.assertTrue(any(("nombre" in linea) and ("archivo" in linea) for linea in out))
