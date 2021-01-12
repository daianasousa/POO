def style(d=27, simbolo='#_'):
    print(d * simbolo)

#nome, ano, cor, velocidade_max, velocidade_atual, estado.
class Carro:
    def __init__(self, velocidade_max, velocidade_atual, estado, nome='sem nome', cor='sem cor', ano='sem ano'):
        self.__velocidade_max = velocidade_max
        self.__velocidade_atual = velocidade_atual
        self.__estado = estado
        self.__nome = nome
        self.__cor = cor
        self.__ano = ano

    #Métodos
    def getnome(self):
        return self.__nome

    def getano(self):
        return self.__ano

    def getcor(self):
        return self.__cor

    def getligar(self):
        self.__estado = True
        return 'Carro ligado'
    
    def getparar(self):
        self.__velocidade_atual = 0
        return 'Carro parado'
    
    def getdesligar(self):
        self.__estado = False
        return 'Carro desligado'
    
    def getacelerar(self, valor):
        if self.__estado == True:
            self.__velocidade_atual = valor
            if self.__velocidade_atual <= self.__velocidade_max:
                return f'A velocidade atual é de {self.__velocidade_atual} km/h'
            else:
                return f'Voçê passou da velocidade máxima permitida de {self.__velocidade_max} Km/h'
            
        elif self.__estado == False:
            return 'Carro desligado'


#Objeto_1
fusca = Carro(velocidade_max=80, velocidade_atual=20, estado=True, nome='Fusca', cor='preto', ano=1965)
print(f'Nome: {fusca.getnome()}')
print(f'Cor: {fusca.getcor()}')
print(f'Ano: {fusca.getano()}')
print(fusca.getacelerar(40))
print(fusca.getdesligar())
print(fusca.getligar())
print(fusca.getacelerar(100))
print(fusca.getdesligar())
print('')
style()
print('')
#Objeto_2
hilux = Carro(velocidade_max=165, velocidade_atual=0, estado=False, nome='Hilux_SRV 4×4 AUT', cor='vermelho', ano=2020) 
print(f'Nome: {hilux.getnome()}')
print(f'Cor: {hilux.getcor()}')
print(f'Ano: {hilux.getano()}')
print(hilux.getacelerar(200))
print(hilux.getligar())
print(hilux.getacelerar(320))
print(hilux.getparar())
print(hilux.getdesligar())