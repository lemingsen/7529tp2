import math

class Dijkstra:
    def __init__(self,grafo,desde):
        cantNodos = grafo.cantidadNodos()
        if (desde < 0) or (desde >= cantNodos):
            raise Exception("El nodo no existe")
        
        self._estadoVisitado = [False    for i in range(cantNodos)]
        self._visitables     = [i        for i in range(cantNodos)]
        self.distancias      = [math.inf for i in range(cantNodos)]
        self.distancias[desde] = 0
        
        while(len(self._visitables)):
            visitando = self._visitar()
            arcos = grafo.arcoDesdeNodoId(visitando)
            for(destino, peso) in arcos:
                if not self._fueVisitado(destino):
                    distanciaAlternativa = self.distancias[visitando] + peso
                    if distanciaAlternativa < self.distancias[destino]:
                        self.distancias[destino] = distanciaAlternativa

    def _visitar(self):
        # Ordenar visitables de menor a mayor distancia
        self._visitables = sorted(self._visitables, key=lambda nodo:self.distancias[nodo])

        aVisitar = self._visitables.pop(0)
        self._estadoVisitado[aVisitar] = True
        return aVisitar

    def _fueVisitado(self, nodo):
        return self._estadoVisitado[nodo]
