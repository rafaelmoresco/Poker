import random
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
    player = Jogador()
    j.append(player)
baralho = Baralho(bar)
mesa = Mesa()
regras = Regras()

while True:
    for i in range(0,10):
        j[i].reset()
    print("Digite o numero de jogadores entre 10 a 2 ou '0' para sair: ", end='')
    nj = int(input())
    if nj == 0:
        break
    elif nj == 1:
        print("Nao eh possivel jogar poker com 1 jogador, tente pelo menos 2")
    elif nj >= 11:
        print("Maximo de 10 jogadores por mesa")
    else:
        jogo = True
        if nj < 10:
            for i in range (0, nj):
                j[i].entrarNoJogo()
        #controle de cada partida
        while jogo:
            baralho.reset(bar)
            mesa.reset()
            baralho.shuffle()
            regras.lista(j)
            baralho.darMesa(mesa)
            baralho.darJogadores(j)
            mesa.mostrarCartas()
            for i in range(0,nj):
                print("Jogador %d:" % (i+1))
                j[i].mostrarMao()
            ''' acho que esse sitema nao vai funcionar
            for i in range(len(regras.listaJogadores)):
                if regras.listaJogadores[i].fD == False:
                    regras.listaJogadores[i].setD()
                    regras.listaJogadores[i].setFD()
                    break
            '''
            jogo = False
