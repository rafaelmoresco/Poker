import random

from pokereval.card import Card
from pokereval.hand_evaluator import HandEvaluator

class Baralho():
    def __init__(self, bar):
        self.baralho = bar
    def reset(self, bar):
        self.baralho = bar
    def shuffle(self):
        random.shuffle(self.baralho)
        print("Barulho de cartas embaralhando")
    def darMesa(self, mesa):
        for i in range (0,5):
            mesa.cartas[i] = self.baralho.pop()
            print("Barulho de carta indo para a mesa")
    def darJogadores(self, j):
        for i in range (0,2):
            for k in range(0, len(j)):
                if j[k].noJogo:
                    j[k].mao[i] = self.baralho.pop()
                    print("Barulho de receber carta")