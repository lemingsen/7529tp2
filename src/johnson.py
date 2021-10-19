from src.dijkstra import Dijkstra

class Johnson:
    def __init__(self, grafo):
        if grafo.cantidadNodos()<1:
            raise Exception("No hay suficientes nodos")

        self.matriz = [Dijkstra(grafo, u).distancias
                        for u in range(grafo.cantidadNodos())]
