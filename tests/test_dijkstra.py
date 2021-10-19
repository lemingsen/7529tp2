import math
import types
import unittest

from src.grafosimple import GrafoSimple
from src.dijkstra import Dijkstra

class TestDijkstra(unittest.TestCase):
    def test_vacio(self):
        grafo = GrafoSimple()
        self.assertRaises(Exception,Dijkstra,grafo,0)

    def test_AB10_desde_menos1_0_1_2(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",10)
        
        self.assertRaises(Exception,Dijkstra,grafo,-1)
        self.assertTrue(isinstance(Dijkstra(grafo,0),Dijkstra))
        self.assertTrue(isinstance(Dijkstra(grafo,1),Dijkstra))
        self.assertRaises(Exception,Dijkstra,grafo,2)
    
    def test_AB10_distancias(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",10)
        dijkstra0 = Dijkstra(grafo,0)
        dijkstra1 = Dijkstra(grafo,1)

        self.assertEqual(list(dijkstra0.distancias), [0, 10])
        self.assertEqual(list(dijkstra1.distancias), [math.inf, 0])
