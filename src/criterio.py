from math import inf

class Criterio:
    def __init__(self, matriz):
        if (not matriz) or (0 == len(matriz)) or (not matriz[0]) or (0 == len(matriz[0])):
            raise Exception("El formato de la matriz no es corrrecto")
        self.mejores = [0]

    @classmethod
    def analizar(cls, distancias):
        infs = sum([1 if inf == distancia else 0 for distancia in distancias])
        suma = 0
        
        return (infs,suma if infs<len(distancias) else inf )