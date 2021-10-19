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

    def test_cantidad_incorrecta_campos(self):
        rutaArchivo = self.pathArchivo("entradas/test_cantidad_incorrecta_campos.txt")
        out = self.ejecutar([rutaArchivo])
        self.assertTrue(self.lineaCumple(out, lambda txt: ("cantidad" in txt) and ("campos" in txt)))

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

    def test_AB6BA7AC1CA2(self):
        rutaArchivo = self.pathArchivo("entradas/test_AB6BA7AC1CA2.txt")
        out = self.ejecutar([rutaArchivo])
        self.assertTrue(self.lineaCumple(out, lambda txt: "recomendada: A" in txt))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([0,6,1],"A")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([7,0,8],"B")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([2,8,0],"C")))

    def test_ejtp2_pos(self):
        """Grafo H del TP2 (todos positivos)"""
        rutaArchivo = self.pathArchivo("entradas/test_ejtp2_pos.txt")
        out = self.ejecutar([rutaArchivo])
        self.assertTrue(self.lineaCumple(out, lambda txt: "recomendada: 5" in txt))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([ 0,14,1,27,18],"1")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([26, 0,1,13,18],"2")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([25,30,0,30,17],"3")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([26, 0,1, 0,18],"4")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([ 8,13,0,13, 0],"5")))

    def test_cormen_pos(self):
        """Ejemplo tomado de Cormen et al. «Intorduction to Algorithms», 3ª ed.
        Corresponde al grafo obtenido luego de aplicar Bellman-Ford."""
        rutaArchivo = self.pathArchivo("entradas/test_cormen_pos.txt")
        out = self.ejecutar([rutaArchivo])
        self.assertTrue(self.lineaCumple(out, lambda txt: "recomendadas: 2, 3, 4" in txt))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([0,2,2,2,0],"1")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([2,0,0,0,2],"2")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([2,0,0,0,2],"3")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([2,0,0,0,2],"4")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([4,2,2,2,0],"5")))

    def test_ciclo_positivo(self):
        rutaArchivo = self.pathArchivo("entradas/test_ciclo_positivo.txt")
        out = self.ejecutar([rutaArchivo])
        self.assertTrue(self.lineaCumple(out, lambda txt: "recomendada: A" in txt))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([0,-5,-15],"A")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([10,0,-10],"B")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([20,15,0],"C")))

    def test_4nodos_con_negativos(self):
        rutaArchivo = self.pathArchivo("entradas/test_4nodos_con_negativos.txt")
        out = self.ejecutar([rutaArchivo])
        self.assertTrue(self.lineaCumple(out, lambda txt: "recomendada: A" in txt))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([0,-4,1,-1],"A")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([inf,0,5,3],"B")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([inf,-5,0,-2],"C")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([inf,-3,2,0],"D")))

    def test_5nodos_con_negativos(self):
        rutaArchivo = self.pathArchivo("entradas/test_5nodos_con_negativos.txt")
        out = self.ejecutar([rutaArchivo])
        self.assertTrue(self.lineaCumple(out, lambda txt: "recomendada: D" in txt))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([ 0,6, 2,7, 5],"A")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([-4,0,-4,1,-1],"B")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([ 0,6, 0,5, 3],"C")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([-5,1,-5,0,-2],"D")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([-3,3,-3,2, 0],"E")))

    def test_cormen(self):
        """Ejemplo tomado de Cormen et al. «Intorduction to Algorithms», 3ª ed."""
        rutaArchivo = self.pathArchivo("entradas/test_cormen.txt")
        out = self.ejecutar([rutaArchivo])
        self.assertTrue(self.lineaCumple(out, lambda txt: "recomendada: 4" in txt))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([0, 1,-3,2,-4], "1")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([3, 0,-4,1,-1], "2")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([7, 4, 0,5, 3], "3")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([2,-1,-5,0,-2], "4")))
        self.assertTrue(self.lineaCumple(out, self.fnMatchFilaYNombre([8, 5, 1,6, 0], "5")))
