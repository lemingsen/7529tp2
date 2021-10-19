class Criterio:
    def __init__(self, matriz):
        if (not matriz) or (0 == len(matriz)) or (not matriz[0]) or (0 == len(matriz[0])):
            raise Exception("El formato de la matriz no es corrrecto")
        self.mejores = [0]