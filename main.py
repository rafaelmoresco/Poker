import random
import numpy as np
import itertools

from baralho import Baralho
from jogador import Jogador
from mesa import Mesa
from regras import Regras

def gerar_cartas():
    valor = ["ás","dois","três","quatro","cinco","seis","sete","oito","nove","dez","valete","dama","rei"]
    naipe = ["espadas","copas","ouros","paus"]
    l = []
    for n in range(4):
        for v in range(13):
            nome_carta = valor[v] + " de " + naipe[n]
            l.append(nome_carta)
    return l

bar = gerar_cartas()
j = []
for k in range(1,11):
    player = []
    j.append(player)

