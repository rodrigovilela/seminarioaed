class Cidade:
    def __init__(self, nome, distanciaObjetivo):
        self.nome = nome
        self.visitado = False
        self.distanciaObjetivo = distanciaObjetivo
        self.adjacentes = []
        
    def addCidadeAdjacentes (self, cidade):
        self.adjacentes.append(cidade)

