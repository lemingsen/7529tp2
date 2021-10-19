import io
import re
import os
import subprocess
import sys
import unittest
from math import inf

class TestTP2(unittest.TestCase):

    ################################ AUXILIARES ################################
    def pathArchivo(self, rutaRelativa):
        return os.path.realpath(os.path.join(os.path.dirname(__file__), rutaRelativa))

    def ejecutar(self,argumentos,guardar=True,charset='windows-1252'):
        args = [sys.executable, "-m", "src.tp2",*argumentos]
        cwd = self.pathArchivo("../")
        self._primera = None
        self._ultima = None

        with subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=None,shell=False,cwd=cwd) as proc:
            primera = proc.stdout.readline().decode(charset)
            if (1 == guardar) or (True is guardar):
                self._primera = primera
            yield primera

            ultima = primera
            while ultima:
                ultima = proc.stdout.readline().decode(charset)
                if not ultima:
                    return
                if (-1 == guardar) or (True is guardar):
                    self._ultima = ultima
                yield ultima

    def fnMatchFilaYNombre(self,fila, nombre):
        """Devuelve una función que verifica si el parámetro coincide con
        el nombre (que también es re) y los valores de fila dados."""
        patternNom  = r"\s*" + nombre + r":\s*"
        patternFila = (r"\s+").join(map(str,fila))
        pattern = patternNom+patternFila
        def fn(txt):
            return re.match(pattern, txt)
        return fn
        
    def lineaCumple(self, lineas, fnTextoEnLinea, verbose=True):
        cumple = any(fnTextoEnLinea(linea) for linea in lineas)
        if verbose and not cumple:
            if self._primera:
                print("Primera: ", self._primera)
            if self._ultima:
                print("Última: ", self._primera)
        return cumple

    def setUp(self):
        self._python = "python"


    ################################ TESTS ################################
    def test_sin_argumentos(self):
        out = self.ejecutar([])

        self.assertTrue(self.lineaCumple(out, lambda txt: ("nombre" in txt) and ("archivo" in txt)))

    def test_inexistente(self):
        rutaArchivo = self.pathArchivo("entradas/nombre_de_archivo_inexistente.txt")
        out = self.ejecutar([rutaArchivo])
        self.assertTrue(self.lineaCumple(out, lambda txt: ("archivo" in txt) and ("inexistente" in txt)))

    def test_vacio(self):
        rutaArchivo = self.pathArchivo("entradas/archivo_vacio.txt")
        out = self.ejecutar([rutaArchivo])
        self.assertTrue(self.lineaCumple(out, lambda txt: "no contiene" in txt))

    def test_AB10(self):
        rutaArchivo = self.pathArchivo("entradas/test_AB10.txt")
        out = self.ejecutar([rutaArchivo])
        self.assertTrue(self.lineaCumple(out, lambda txt: "recomendada: A" in txt))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([0,10],"A")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([inf,0],"B")))
        
    def test_BA5_sin_retorno(self):
        rutaArchivo = self.pathArchivo("entradas/test_BA5_sin_retorno.txt")
        out = self.ejecutar([rutaArchivo])
        self.assertTrue(self.lineaCumple(out, lambda txt: "recomendada: B" in txt))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([0,5],"B")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([inf,0],"A")))

    def test_BA_menos5(self):
        rutaArchivo = self.pathArchivo("entradas/test_BA_menos5.txt")
        out = self.ejecutar([rutaArchivo])
        self.assertTrue(self.lineaCumple(out, lambda txt: "recomendada: B" in txt))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([0,-5],"B")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([inf,0],"A")))

    def test_3arcos(self):
        rutaArchivo = self.pathArchivo("entradas/test_3arcos.txt")
        out = self.ejecutar([rutaArchivo])
        self.assertTrue(self.lineaCumple(out, lambda txt: "recomendada: A" in txt))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([0,54,-3,62],"A")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([inf,0,inf,8],"B")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([inf,inf,0,inf],"D")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([inf,inf,inf,0],"C")))

