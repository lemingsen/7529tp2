from math import inf
import unittest

from src.criterio import Criterio

class TestCriterio(unittest.TestCase):
    def test_vacio(self):
        self.assertRaises(Exception,Criterio,None)
        self.assertRaises(Exception,Criterio,[])
        self.assertRaises(Exception,Criterio,[[]])

    def test_1x1(self):
        criterio = Criterio([[inf]])
        self.assertEqual(criterio.mejores, [0])

    def test_analizar_inf(self):
        self.assertEqual(Criterio.analizar([inf]), (1,inf))

    def test_analizar_inf0(self):
        self.assertEqual(Criterio.analizar([inf,0]), (1,0))

    def test_analizar_menos10inf(self):
        self.assertEqual(Criterio.analizar([-10,inf]), (1,-10))

    def test_analizar_inf20inf(self):
        self.assertEqual(Criterio.analizar([inf,20,inf]), (2,20))

    def test_analizar_inf20inf(self):
        self.assertEqual(Criterio.analizar([-6,inf,13,inf]), (2,7))

