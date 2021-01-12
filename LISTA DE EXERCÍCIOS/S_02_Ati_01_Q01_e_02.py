class Carro:
    #Atributos
    nome = None
    ano = None
    cor = None
    veloc_max = None
    veloc_atual = 0
    estado = 'Desligado'

    #Construtores
    def __init__(self, cor, nome, veloc_max):
        self.cor = cor
        self.nome = nome
        self.veloc_max = veloc_max

    #Métodos
    def ligar(self):
        self.estado = 'Ligado'
        
        if self.nome == 'Fusca':
            print('O Fusca está ligado.')
        else:
            print('A Ferrari está ligada.')

    
    def parar(self):
        self.veloc_atual = 0
        
        if self.nome == 'Fusca':
            print('Seu Fusca está Parado.')
        else:
            print('Sua Ferrari está Parada.')
    
    def desligar(self):
        self.estado = 'Desligado'
        if self.nome == 'Fusca':
            print('Seu Fusca está desligado.')
        else:
            print('Sua Ferrari está desligada.')


    def acelerar(self, valor):
        if self.nome == 'Fusca':
            if self.estado == 'Ligado':
                self.veloc_atual = valor
                if self.veloc_atual <= self.veloc_max:
                    print(f'A velocidade atual do Fusca é de {fusca.veloc_atual} km/h.')
                else:
                    print(f'Voçê passou da velocidade máxima do Fusca que era de {self.veloc_max} Km/h.')
            
            elif self.estado == 'Desligado':
                print('O Fusca está desligado.')
        else:
            if self.estado == 'Ligado':
                self.veloc_atual = valor
                if self.veloc_atual <= self.veloc_max:
                    print(f'A velocidade atual da Ferrrari é de {fusca.veloc_atual} km/h.')
                else:
                    print(f'Voçê passou da velocidade máxima da Ferrari que era de {self.veloc_max} Km/h.')
            
            elif self.estado == 'Desligado':
                print('A Ferrari está desligada.') 

#Objetos
fusca = Carro('preto', 'Fusca', 80)
fusca.nome = 'Fusca'
fusca.ano = 1965
fusca.cor = 'preto'
fusca.veloc_max = 80
fusca.veloc_atual = 20
fusca.estado = 'ligado'
ferrari_sr2000 = Carro('vermelho', 'ferrari_sr2000', 300) 
ferrari_sr2000.nome = 'ferrari_sr2000'
ferrari_sr2000.ano = 2014
ferrari_sr2000.cor = 'vermelho'
ferrari_sr2000.veloc_max = 300
ferrari_sr2000.veloc_atual = 0
ferrari_sr2000.estado = 'desligado'
fusca.acelerar(40)
ferrari_sr2000.acelerar(200)
fusca.desligar()
ferrari_sr2000.ligar()
ferrari_sr2000.acelerar(320)
ferrari_sr2000.parar()
ferrari_sr2000.desligar()
fusca.ligar()
fusca.acelerar(100)
fusca.desligar()