from src.grafosimple import GrafoSimple

class Lector:
    def __init__(self, nombreArchivo,verbose=False):
        self._verbose = verbose
        with open(nombreArchivo, "r") as archivo:
            if self._verbose:
                print("\nArchivo: ",nombreArchivo)

            self.grafo = GrafoSimple()
            lineas = self._lineas(archivo)
            entradas = (self._parsear(linea) for linea in lineas if linea)
            for entrada in entradas:
                if entrada:
                    self.grafo.insertarArcoConAlias(entrada[0], entrada[1], int(entrada[2]))

    def _lineas(self,archivo):
        while True:
            leido = archivo.readline()
            if not leido:
                return
            linea = leido.strip() if leido else None
            if linea:
                if self._verbose:
                    print(" Línea: ",linea)
                yield linea
            else:
                if self._verbose:
                    print(" Ignorando leído:", leido)

    def _parsear(self,linea):
        campos = linea.split(',')
        if (not campos) or (0 == len(campos)):
            if self._verbose:
                print("  Ignorando campos: ",linea)
            return None
        entrada = list(map(lambda campo: campo.strip(), campos))
        if self._verbose:
            print("Entrada: ",entrada)

        return entrada