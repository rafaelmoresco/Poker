import random

class Baralho():
    def __init__(self, bar):
        self.baralho = bar
    def reset(self):
        self.baralho = bar
    def shuffle(self, bar):
        random.shuffle(self.baralho)
    def darMesa(self, mesa):
        for i in range (0,5):
            mesa.cartas[i] = self.baralho.pop()
    def darJogadores(self, j):
        for i in range (0,2):
            for k in range(1, len(j)):
                if j[k].noJogo:
                    j[k].mao[i] = self.baralho.pop()