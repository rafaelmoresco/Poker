
class Regras():
    def __init__(self):
        pass
    
    def lista(self, j):
        self.listaJogadores = []
        for k in range(0, len(j)):
            if j[k].noJogo:
                self.listaJogadores.append(j[k])

    def posicao(self):
        for i in self.listaJogadores:
            if self.listaJogadores[i].d == True:
                self.listaJogadores[i-1].setSB()
                self.listaJogadores[i-2].setBB()

    #def pontuacao(self):

