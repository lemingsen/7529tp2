from src.grafosimple import GrafoSimple

class Lector:
    def __init__(self, nombreArchivo):
        with open(nombreArchivo, "r") as archivo:
            self.grafo = GrafoSimple()
            lineas = self._lineas(archivo)
            entradas = (self._parsear(linea) for linea in lineas if linea)
            for entrada in entradas:
                if entrada:
                    self.grafo.insertarArcoConAlias(entrada[0], entrada[1], int(entrada[2]))

    def _lineas(self,archivo):
        while True:
            linea = archivo.readline()
            linea = linea.strip() if linea else None
            if linea:
                yield linea
            else:
                return

    def _parsear(self,linea):
        campos = linea.split(',')
        if (not campos) or (0 == len(campos)):
            return None
        return list(map(lambda campo: campo.strip(), campos))