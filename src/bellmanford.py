class BellmanFordConCeroAgregado:
    def __init__(self,grafo):
        cantNodos = grafo.cantidadNodos()
        if cantNodos<1:
            raise Exception("")
        self.distancias = [0 for i in range(cantNodos)]

