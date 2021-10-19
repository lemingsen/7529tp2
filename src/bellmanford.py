class BellmanFordConCeroAgregado:
    def __init__(self,grafo):
        cantNodos = grafo.cantidadNodos()
        if cantNodos<1:
            raise Exception("")
        # En la primera iteración real de Beellman-Ford, como el nodo
        # agregado tiene arcos de peso 0, todos pasan a tener esa distancia.
        self.distancias = [0 for i in range(cantNodos)]

        for (origen,destino,peso) in grafo.arcos():
            distanciaAlternativa = self.distancias[origen] + peso
            if distanciaAlternativa < self.distancias[destino]:
                self.distancias[destino] = distanciaAlternativa
