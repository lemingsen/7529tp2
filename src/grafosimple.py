class GrafoSimple:
    def __init__(self):
        self._cantidadNodos = 0
        self._cantidadArcos = 0
        self._listaAlias = dict()

    def cantidadNodos(self):
        return self._cantidadNodos

    def cantidadArcos(self):
        return self._cantidadArcos

    def insertarArcoConAlias(self, aliasOrigen, aliasDestino, peso):
        self.idDeNodoAlias(aliasOrigen)
        self.idDeNodoAlias(aliasDestino)
        self._cantidadArcos += 1

    def idDeNodoAlias(self, aliasNodo):
        if aliasNodo in self._listaAlias:
            return self._listaAlias[aliasNodo]
        else:
            nuevoId = self._cantidadNodos
            self._cantidadNodos += 1
            self._listaAlias[aliasNodo] = nuevoId
            return nuevoId
