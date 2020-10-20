import random
import itertools

from baralho import Baralho
from jogador import Jogador
from mesa import Mesa
from regras import Regras
from pokereval.card import Card
from pokereval.hand_evaluator import HandEvaluator

bars = [Card(2,"s"),Card(3,"s"),Card(4,"s"),Card(5,"s"),Card(6,"s"),Card(7,"s"),Card(8,"s"),Card(9,"s"),Card(10,"s"),Card("J","s"),Card("Q","s"),Card("K","s"),Card("A","s")]
barh = [Card(2,"h"),Card(3,"h"),Card(4,"h"),Card(5,"h"),Card(6,"h"),Card(7,"h"),Card(8,"h"),Card(9,"h"),Card(10,"h"),Card("J","h"),Card("Q","h"),Card("K","h"),Card("A","h")]
barc = [Card(2,"c"),Card(3,"c"),Card(4,"c"),Card(5,"c"),Card(6,"c"),Card(7,"c"),Card(8,"c"),Card(9,"c"),Card(10,"c"),Card("J","c"),Card("Q","c"),Card("K","c"),Card("A","c")]
bard = [Card(2,"d"),Card(3,"d"),Card(4,"d"),Card(5,"d"),Card(6,"d"),Card(7,"d"),Card(8,"d"),Card(9,"d"),Card(10,"d"),Card("J","d"),Card("Q","d"),Card("K","d"),Card("A","d")]

bar = bars + barh + barc + bard

j = []
for k in range(1,9):
    player = Jogador(k)
    j.append(player)
baralho = Baralho(bar)
baralho2 = Baralho(bar)
mesa = Mesa()
regras = Regras()

while True:
    for i in range(0,8):
        j[i].reset()
    print("Digite o numero de jogadores entre 8 a 2 ou '0' para sair: ", end='')
    nj = int(input())
    if nj == 0:
        break
    elif nj == 1:
        print("Nao eh possivel jogar poker com 1 jogador, tente pelo menos 2")
    elif nj >= 9:
        print("Maximo de 8 jogadores por mesa")
    else:
        jogo = True
        for i in range (0, nj):
            j[i].entrarNoJogo()
        #controle de cada partida
        rodada = 0
        print("Defina o small blind: ", end='')
        sbp = int(input())
        j[0].setD()
        while jogo:
            for i in range(0, len(j)):
                j[i].novaRodada()
            jSobrando = 0
            for i in range(0, len(j)):
                if j[i].noJogo:
                    jSobrando += 1
            if jSobrando < 2:
                jogo = False
            
            #cria um baralho novo
            bars = [Card(2,"s"),Card(3,"s"),Card(4,"s"),Card(5,"s"),Card(6,"s"),Card(7,"s"),Card(8,"s"),Card(9,"s"),Card(10,"s"),Card("J","s"),Card("Q","s"),Card("K","s"),Card("A","s")]
            barh = [Card(2,"h"),Card(3,"h"),Card(4,"h"),Card(5,"h"),Card(6,"h"),Card(7,"h"),Card(8,"h"),Card(9,"h"),Card(10,"h"),Card("J","h"),Card("Q","h"),Card("K","h"),Card("A","h")]
            barc = [Card(2,"c"),Card(3,"c"),Card(4,"c"),Card(5,"c"),Card(6,"c"),Card(7,"c"),Card(8,"c"),Card(9,"c"),Card(10,"c"),Card("J","c"),Card("Q","c"),Card("K","c"),Card("A","c")]
            bard = [Card(2,"d"),Card(3,"d"),Card(4,"d"),Card(5,"d"),Card(6,"d"),Card(7,"d"),Card(8,"d"),Card(9,"d"),Card(10,"d"),Card("J","d"),Card("Q","d"),Card("K","d"),Card("A","d")]
            bar = bars + barh + barc + bard
            baralho.reset(bar)
            
            mesa.reset()
            baralho.shuffle()
            regras.lista(j)
            baralho.darMesa(mesa)
            baralho.darJogadores(j)
            for i in range(0,len(j)):
                print("Jogador %d:" % (i+1))
                j[i].mostrarMao()
            regras.posicao(rodada)
            #determinar a ordem das apostas
            for i in range(0,len(regras.listaJogadores)):
                if regras.listaJogadores[i].sb:
                    regras.listaJogadores[i].aposta(mesa,sbp)
                    print("Jogador %d pagou %d de Small Blind" % (regras.listaJogadores[i].n, sbp))
                elif regras.listaJogadores[i].bb:
                    regras.listaJogadores[i].aposta(mesa,2*sbp)
                    print("Jogador %d pagou %d de Big Blind" % (regras.listaJogadores[i].n, 2*sbp))
            novalista = [0]*len(regras.listaJogadores)
            for i in range(0,len(regras.listaJogadores)):
                if j[i].d == True:
                    inicio = i
                    break
            for i in range(0,len(regras.listaJogadores)):
                novalista[i] = j[(i + inicio) % len(regras.listaJogadores)]
            for k in range(0,4):
                if k >= 1:
                    mesa.mostrarCartas()
                for i in range(0,len(novalista)):
                    novalista[i].cobriu = False
                i = 0
                while True:
                    if i == len(novalista):
                        i = 0
                    jForaDaRodada = 0
                    for verDesistentes in range(0, len(novalista)):
                        if (novalista[verDesistentes].naRodada == False):
                            jForaDaRodada += 1
                    if jForaDaRodada > len(novalista)-2:
                        break
                    if novalista[i].cobriu and novalista[i].apostaAtual == mesa.apostaMaior:
                        break
                    if novalista[i].naRodada == True:
                        while True:
                            print("Aposta atual: %d\nMesa: %d\nO jogador %d deseja: \n 1. Aumentar a aposta; \n 2. Cobrir a aposta; \n 3. Desistir?"%(mesa.apostaMaior, mesa.dinheiroTotal, novalista[i].n))
                            opcao = int(input())
                            if opcao == 1:
                                print("Insira valor extra: ", end='')
                                x = int(input())
                                novalista[i].aumentarAposta(mesa, x)
                                novalista[i].cobriu = True
                                break
                            elif opcao == 2:
                                novalista[i].cobrirAposta(mesa)
                                novalista[i].cobriu = True
                                break
                            elif opcao == 3:
                                novalista[i].desistir()
                                break
                            else:
                                print("Opção inválida")
                    i += 1
            regras.pontuacao(novalista, mesa)
            mesa.distribuirDinheiro(novalista)
            for i in range(0,nj):
                print("Jogador %d: %d" % (novalista[i].n, novalista[i].dinheiro))
            rodada += 1