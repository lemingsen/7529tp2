class GrafoSimple:
    def __init__(self):
        self._cantidadNodos = 0
        self._cantidadArcos = 0

    def cantidadNodos(self):
        return self._cantidadNodos

    def cantidadArcos(self):
        return self._cantidadArcos

    def insertarArcoConAlias(self, aliasOrigen, aliasDestino, peso):
        self._cantidadNodos += 2
        self._cantidadArcos += 1


