from math import inf
import unittest

from src.criterio import Criterio

class TestJohnson(unittest.TestCase):
    def test_vacio(self):
        self.assertRaises(Exception,Criterio,None)
        self.assertRaises(Exception,Criterio,[])
        self.assertRaises(Exception,Criterio,[[]])
