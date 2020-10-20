from pokereval.card import Card
from pokereval.hand_evaluator import HandEvaluator

class Regras():
    def __init__(self):
        pass
    
    def lista(self, j):
        self.listaJogadores = []
        for k in range(0, len(j)):
            if j[k].noJogo:
                self.listaJogadores.append(j[k])

    def posicao(self, rodada):
        if rodada > len(self.listaJogadores):
            rodada = 0
        for i in range(len(self.listaJogadores)):
            if i == rodada:
                self.listaJogadores[i].d = True
            else:
                self.listaJogadores[i].removeToken()
        for i in range(len(self.listaJogadores)):
            if self.listaJogadores[i].d == True:
                self.listaJogadores[i-2].setSB()
                self.listaJogadores[i-1].setBB()

    def pontuacao(self, j, mesa):
        score = 0
        for i in range(len(j)):
            if ((j[i].noJogo == True) and (j[i].naRodada == True)):
                j[i].score = HandEvaluator.evaluate_hand(j[i].mao, mesa.cartas)
        for i in range(len(j)):
            if ((j[i].noJogo == True) and (j[i].naRodada == True)):
                if j[i].score > score:
                    score = j[i].score
        for i in range(len(j)):
            if ((j[i].noJogo == True) and (j[i].naRodada == True)):
                if score == j[i].score:
                    j[i].venceuRodada()
                    print("Jogador %d venceu rodada" % (j[i].n))


