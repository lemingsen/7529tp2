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

    def test_AB5BA20_distancias(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",5)
        grafo.insertarArcoConAlias("B","A",20)
        dijkstra0 = Dijkstra(grafo,0)
        dijkstra1 = Dijkstra(grafo,1)

        self.assertEqual(list(dijkstra0.distancias), [0, 5])
        self.assertEqual(list(dijkstra1.distancias), [20, 0])

    def test_AB1BA2xA0_distancias(self):
        grafo = GrafoSimple()
        x = object()
        grafo.insertarArcoConAlias("A","B",1)
        grafo.insertarArcoConAlias("B","A",2)
        grafo.insertarArcoConAlias(x,"A",0)
        
        dijkstra0 = Dijkstra(grafo,0)
        dijkstra1 = Dijkstra(grafo,1)
        dijkstrax = Dijkstra(grafo,2)

        self.assertEqual(list(dijkstra0.distancias), [0, 1, math.inf])
        self.assertEqual(list(dijkstra1.distancias), [2, 0, math.inf])
        self.assertEqual(list(dijkstrax.distancias), [0, 1, 0])

    def test_ejtp2(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("1","2",14)
        grafo.insertarArcoConAlias("1","3",1)
        grafo.insertarArcoConAlias("2","3",1)
        grafo.insertarArcoConAlias("2","4",13)
        grafo.insertarArcoConAlias("3","5",17)
        grafo.insertarArcoConAlias("4","2",0)
        grafo.insertarArcoConAlias("5","1",8)
        grafo.insertarArcoConAlias("5","3",0)
        grafo.insertarArcoConAlias("5","4",13)

        matriz = [Dijkstra(grafo,i).distancias for i in range(5)]

        self.assertEqual(matriz[0], [ 0,14,1,27,18])
        self.assertEqual(matriz[1], [26, 0,1,13,18])
        self.assertEqual(matriz[2], [25,30,0,30,17])
        self.assertEqual(matriz[3], [26, 0,1, 0,18])
        self.assertEqual(matriz[4], [ 8,13,0,13, 0])
