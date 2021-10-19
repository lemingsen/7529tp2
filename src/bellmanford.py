class BellmanFordConCeroAgregado:
    def __init__(self,grafo):
        """Crea una instancia con las distancias para un grafo copia del
        dado, al que se añade un nodo con arcos de peso 0 hacia el resto
        de los nodos (pero sin nodo que llegue al mismo). Las distancias
        serán calculandas con Bellman-Ford¹ para el nodo agregado, pero
        sólo se devolverá las de los demás nodos.

        ¹ Sabiendo que el nodo agregado no tiene nodos de entrada por lo
        que no puede cambiar su distancia, y entonces desde ella hasta
        otros siempre será 0, en esta implementación no se almacena."""
        cantNodos = grafo.cantidadNodos()
        cantArcosCon0 = grafo.cantidadArcos() + grafo.cantidadNodos()
        self._arcos = list(grafo.arcos())

        if cantNodos<1:
            raise Exception("")
        # En la primera iteración real de Beellman-Ford, como el nodo
        # agregado tiene arcos de peso 0, todos pasan a tener esa distancia.
        self.distancias = [0 for i in range(cantNodos)]

        for k in range(cantArcosCon0 - 1):
            self._iterar()
            # Finalización temprana:
            if(not self._huboCambio):
                break

        # Comprobar bucle
        self._iterar()
        if(self._huboCambio):
            self.distancias = False

    def _iterar(self):
        self._huboCambio = False
        for (origen,destino,peso) in self._arcos:
            distanciaAlternativa = self.distancias[origen] + peso
            if distanciaAlternativa < self.distancias[destino]:
                self.distancias[destino] = distanciaAlternativa
                self._huboCambio = True
