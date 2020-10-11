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

    def posicao(self):
        for i in self.listaJogadores:
            if self.listaJogadores[i].d == True:
                self.listaJogadores[i-1].setSB()
                self.listaJogadores[i-2].setBB()

    def pontuacao(self, j, mesa):
        score = 0
        for i in range(len(j)):
            if j[i].noJogo:
                j[i].score = HandEvaluator.evaluate_hand(j[i].mao, mesa.cartas)
        for i in range(len(j)):
            if j[i].noJogo:
                if j[i].score > score:
                    score = j[i].score
        for i in range(len(j)):
            if j[i].noJogo:
                if score == j[i].score:
                    j[i].venceuRodada()
                    print("Jogador %d venceu rodada" % (i+1))


