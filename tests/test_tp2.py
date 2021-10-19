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
        return subprocess.run(args,stdout=subprocess.PIPE)

    def test_sin_argumentos(self):
        proc = self.ejecutar([])
        