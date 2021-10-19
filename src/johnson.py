class Johnson:
    def __init__(self, grafo):
        if grafo.cantidadNodos()<1:
            raise Exception("No hay suficientes nodos")
        self.matriz = []
