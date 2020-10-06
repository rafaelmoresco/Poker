class Regras():
    def __init__(self):
        pass
    
    def lista(self, j):
        self.listaJogadores = []
        for k in range(1, len(j)):
            if j[k].noJogo:
                self.listaJogadores.append(j[k])

    def posicao(self):
        for i in self.listaJogadores:
            if self.listaJogadores[i].d == True:
                setSB(self.listaJogadores[i-1])
                setBB(self.listaJogadores[i-2])

            
