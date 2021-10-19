from src.bellmanford import BellmanFordConCeroAgregado
from src.dijkstra import Dijkstra

class Johnson:
    def __init__(self, grafo):
        if grafo.cantidadNodos()<1:
            raise Exception("No hay suficientes nodos")

        if any(peso<0 for (u,v,peso) in grafo.arcos()):
            h = BellmanFordConCeroAgregado(grafo).distancias
            grafo.modificarPesos( lambda w,u,v: w +h[u] -h[v] )
        else:
            h = [0 for i in range(grafo.cantidadNodos())]
        self.h = h
        
        self.matriz = []
        for u in range(grafo.cantidadNodos()):
            d = Dijkstra(grafo, u).distancias
            self.matriz.append([ d[v] + h[v] -h[u] for v in range(grafo.cantidadNodos()) ])
