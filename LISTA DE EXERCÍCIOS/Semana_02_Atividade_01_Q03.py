class Objeto:
    Marca = None
    Cor = None
    Ano = None
    Processador = 3.6
    Ram = 4
    Velocidade = 3
    Tamanho = None
    Estado = None

    #Construtores
    def __init__(self, Marca, Cor):
        self.Marca = Marca
        self.Cor = Cor
        
    
    def ligar(self, Estado):
        self.Estado = 'Ligado'
        print(self.Estado)

    def desligar(self, Estado):
        self.Estado = 'Desligado'
        print(self.Estado)

    def ram(self):
        self.Ram -= 1
        print(f'Uso da Ram Notebook: {self.Ram} Gb')

    def processador(self):
        self.Processador -= 1
        print(f'O processador do notebook após bastante tempo de uso ficará de: {self.Processador} GHz.')

    def velocidade(self):
        self.Velocidade -= 1
        print(f'A velocidade atual do ventilador está na: {self.Velocidade} potência')

#objetos
Notebook = Objeto('HP', 4)
Marca = 'HP'
Cor = 'Cinza'
Ano = 2007
Memoria = 500
Ram = 4
Processador = 3.6
Tamanho = 14
Estado = 'Desligado'

Ventilador = Objeto('Britania', 3)
Marca = 'Britania'
Cor = 'Preto'
Ano = 2017
Velocidade = 3
Tamanho = 40
Estado = 'Ligado'

#liga o notebook
Notebook.ligar('Ligado')
#marca do ventilador
print(f'A marca do seu ventilador e da {Ventilador.Marca}')
#desliga seu ventilador
Ventilador.desligar('Desligado')
#marca do notebook
print(f'A marca do seu notebook e da {Notebook.Marca}')
#O valor atual da ram do notebook
Notebook.ram()
#O valor atual do Processador do notebook
Notebook.processador()
#Velocidade atual do Ventilador
Ventilador.velocidade()
#desligar os objetos.
Notebook.desligar('desligado')
Ventilador.desligar('desligado')