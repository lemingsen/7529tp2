class Dijkstra:
    def __init__(self,grafo,desde):
        cantNodos = grafo.cantidadNodos()
        if (desde < 0) or (desde >= cantNodos):
            raise Exception("El nodo no existe")
