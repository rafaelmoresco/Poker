
class Mesa():
    def __init__(self):
        self.cartas = [None, None, None, None, None]
        self.apostaMaior = 0
        self.dinheiroTotal = 0
        self.mostrar = 0
    
    def reset(self):
        self.cartas = [None, None, None, None, None]
        self.apostaMaior = 0
        self.dinheiroTotal = 500
        self.mostrar = 0
    
    def mostrarCartas(self):
        if self.mostrar == 0:
            for i in range(0,3):
                print(self.cartas[i], end=' ')
            print()
            self.mostrar = 1
        elif self.mostrar == 1:
            for i in range(0,4):
                print(self.cartas[i], end=' ')
            print()
            self.mostrar = 2
        else:
            for i in range(0,5):
                print(self.cartas[i], end=' ')
            print()
    
    def distribuirDinheiro(self, j):
        k = 0
        dist = []
        for i in range(len(j)):
            if j[i].vencedorRodada == True:
                k += 1
                dist.append(i)
        temp = self.dinheiroTotal%k
        dinheiroDist = (self.dinheiroTotal-temp)/k
        for i in range(len(dist)):
           j[dist[i]].dinheiro += dinheiroDist