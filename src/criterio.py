from math import inf

class Criterio:
    def __init__(self, matriz):
        if (not matriz) or (0 == len(matriz)) or (not matriz[0]) or (0 == len(matriz[0])):
            raise Exception("El formato de la matriz no es corrrecto")
        self.analisis = list(map(Criterio.analizar,matriz))
        self.mejores = [0]


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

