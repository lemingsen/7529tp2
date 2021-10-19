from math import inf

class CriterioError(Exception):
    pass

class Criterio:
    def __init__(self, matriz):
        if (not matriz) or (0 == len(matriz)) or (not matriz[0]) or (0 == len(matriz[0])):
            raise CriterioError("El formato de la matriz no es corrrecto")
        self.analisis = list(map(Criterio.analizar, matriz))
        ids = range(len(matriz))

        costos = list(map(lambda an: an[1], self.analisis))
        self.mejorCosto = min(costos)
        self.mejoresCosto = [id for id in ids if costos[id] == self.mejorCosto]

        limite = list(map(lambda an: an[0], self.analisis))
        self.mejorLimite = min(limite)
        self.mejoresLimite = [id for id in ids if limite[id] == self.mejorLimite]

        self.mejores = self._mejores()


    @classmethod
    def analizar(cls, distancias):
        infs = 0
        suma = 0
        for distancia in distancias:
            if inf == distancia:
                infs += 1
            else:
                suma += distancia
        validos = len(distancias) - infs
        if validos > 0:
            suma = suma / validos
        else:
            suma = inf
        
        return (infs,suma)

    def _mejores(self):
        ambos = list(set(self.mejoresCosto) & set(self.mejoresLimite))
        return ambos if len(ambos) else None