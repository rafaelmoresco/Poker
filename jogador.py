
class Jogador():
    def __init__(self,n):
        self.mao = [None, None]
        self.dinheiro = 500
        self.apostaAtual = 0
        self.noJogo = False
        self.naRodada = True
        self.score = 0
        #nao sei direito o que significa, mas o que to jogando parece indicar quem começa a rodada
        #bb e sb (blinds) são as apostas necessárias para começar o jogo
        self.bb = False
        self.sb = False
        self.d = False
        #variavel de controle extra, diz se ja foi o dealer durante o jogo
        self.cobriu = False
        self.n = n
        
        self.allIn = False
        self.vencedorRodada = False

    def reset(self):
        self.mao = [None, None]
        self.dinheiro = 500
        self.apostaAtual = 0
        self.noJogo = False
        self.naRodada = True
        self.score = 0
        #nao sei direito o que significa, mas o que to jogando parece indicar quem começa a rodada
        #bb e sb (blinds) são as apostas necessárias para começar o jogo
        self.bb = False
        self.sb = False
        self.d = False
        self.cobriu = False
        
        self.allIn = False
        self.vencedorRodada = False
    
    def foraDoJogo(self):
        self.noJogo = False
    
    def entrarNoJogo(self):
        self.noJogo = True
    
    def novaRodada(self):
        self.mao = [None, None]
        self.vencedorRodada = False
        self.naRodada = True
        self.allIn = False
        self.score = 0
        if self.dinheiro <= 0:
            self.foraDoJogo()
    
    def venceuRodada(self):
        self.vencedorRodada = True

    def mostrarMao(self):
        for i in range (0,2):
            print(self.mao[i], end=' ')
        print()
    
    def setBB(self):
        self.bb = True
        self.sb = False
        self.d = False

    def setSB(self):
        self.bb = False
        self.sb = True
        self.d = False

    def setD(self):
        self.bb = False
        self.sb = False
        self.d = True
    
    def setFD(self):
        self.fD = True

    def removeToken(self):
        self.bb = False
        self.sb = False
        self.d = False
    
    def aposta(self, mesa, x):
        self.dinheiro -= x
        self.apostaAtual = x
        mesa.dinheiroTotal += x
        if mesa.apostaMaior < x:
            mesa.apostaMaior = x
    #função para aumentar a aposta na mesa
    def aumentarAposta(self, mesa, x):
        if self.apostaAtual == mesa.apostaMaior:
            self.dinheiro -= x
            self.apostaAtual += x
            mesa.dinheiroTotal += x
            if self.dinheiro <= 0:
                self.allIn = True
        else:
            self.dinheiro -= mesa.apostaMaior - x
            mesa.dinheiroTotal += x
            self.apostaAtual = mesa.apostaMaior + x
            if self.dinheiro <= 0:
                self.allIn = True
        mesa.apostaMaior += x 
    #função para cobrir a aposta atual
    def cobrirAposta(self, mesa):
        if self.dinheiro <= mesa.apostaMaior - self.apostaAtual:
            self.allIn = True
            self.dinheiro = 0
        self.dinheiro -= mesa.apostaMaior - self.apostaAtual
        mesa.dinheiroTotal += mesa.apostaMaior - self.apostaAtual
        self.apostaAtual = mesa.apostaMaior
    
    def desistir(self):
        self.naRodada = False