def style(d=27, simbolo='#_'):
    print(d * simbolo)

#nome, ano, cor, velocidade_max, velocidade_atual, estado.
class Carro:
    def __init__(self, velocidade_max, velocidade_atual, estado, nome='sem nome', cor='sem cor', ano='sem ano'):
        self.velocidade_max = velocidade_max
        self.velocidade_atual = velocidade_atual
        self.estado = estado
        self.nome = nome
        self.cor = cor
        self.ano = ano

    #Métodos
    def ligar(self):
        self.estado = True
        print('Carro ligado')
    
    def parar(self):
        self.velocidade_atual = 0
        print('Carro parado')
    
    def desligar(self):
        self.estado = False
        print('Carro desligado')
    
    def acelerar(self, valor):
        if self.estado == True:
            self.velocidade_atual = valor
            if self.velocidade_atual <= self.velocidade_max:
                print(f'A velocidade atual é de {self.velocidade_atual} km/h')
            else:
                print(f'Voçê passou da velocidade máxima permitida de {self.velocidade_max} Km/h')
            
        elif self.estado == False:
            print('Carro desligado')


#Objeto_1
fusca = Carro(velocidade_max=80, velocidade_atual=20, estado=True, nome='Fusca', cor='preto', ano=1965)
print(f'Nome: {fusca.nome}')
print(f'Cor: {fusca.cor}')
print(f'Ano: {fusca.ano}')
fusca.acelerar(40)
fusca.desligar()
fusca.ligar()
fusca.acelerar(100)
fusca.desligar()
print('')
style()
print('')
#Objeto_2
hilux = Carro(velocidade_max=165, velocidade_atual=0, estado=False, nome='Hilux_SRV 4×4 AUT', cor='vermelho', ano=2020) 
print(f'Nome: {hilux.nome}')
print(f'Cor: {hilux.cor}')
print(f'Ano: {hilux.ano}')
hilux.acelerar(200)
hilux.ligar()
hilux.acelerar(320)
hilux.parar()
hilux.desligar()