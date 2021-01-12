class Radio:
    #Construtores
    def __init__(self, ligado, cor, faixa, peso, altura, estacao, volume, volume_max=100, volume_min=0):
        self.ligado = ligado
        self.cor = cor
        self.faixa = faixa
        self.peso = peso
        self.altura = altura
        self.estacao = estacao
        self.volume = volume
        self.volume_min = volume_min
        self.__volume_max = volume_max

    @property
    def volume_max(self):
        return self.__volume_max

    @volume_max.setter
    def volume_max(self, valor):
        self.__volume_max = valor

    def __str__(self):
        return f'Estado: {self.ligado}\nCor: {self.cor}\nFaixa: {self.faixa}\nPeso: {self.peso}\nAltura: {self.altura} cm\nEstação: {self.estacao}\nVolume: {self.volume}\nVolume_Max: {self.volume_max}\nVolume_Min: {self.volume_min}'

    #Métodos
    def ligar(self):
        if self.ligado == False:
            self.ligado  = True
            print('Rádio ligado')
        else:
            print('Rádio já estava ligado')

    def desligar(self):
        if self.ligado == True:
            self.ligado = False
            print('Rádio desligado')
        else:
            print('Rádio já desligado')

    def mudar_faixa(self, valor):
        self.faixa = valor
        print(f'Faixa: {self.faixa}')

    def passar_volume(self, valor):
        self.volume = valor
        if self.volume > self.__volume_max:
            print('Passou do volume máximo permitido.')
        
        elif self.volume < self.volume_min:
            print('Passou do volume minimo permitido.')
        else:
            print(f'Volume atual: {self.volume}')

    def mudar_estação(self, valor):
        if self.ligado == True:
            self.estacao = valor
            print(f'Estação atual: {self.estacao}')
        else:
            print('Primeiramente ligue seu rádio')

    def passar_estação(self):
        self.estacao += 0.1
        print(f'Passei a estação para {self.estacao:.1f}')

    def aumentar_volume(self):
        self.volume += 1
        if self.volume > self.__volume_max:
            print('Passou do volume máximo permitido.')
        print(f'volume atual: {self.volume}')

    def diminuir_volume(self):
        self.volume -= 1
        if self.volume < self.volume_min:
            print('Passou do volume minimo permitido.')
        print(f'volume atual: {self.volume}')

#Objeto_1
print('=='*10,'RÁDIO DO VOVÔ','=='*10)
radio_do_vovo = Radio(ligado=True, cor='cinza', faixa='AM', peso=2, altura=20, estacao=99.0, volume=15)
print(radio_do_vovo)
radio_do_vovo.mudar_estação(99.2)
radio_do_vovo.passar_estação()
radio_do_vovo.aumentar_volume()
radio_do_vovo.desligar()
print('')
#Objeto_2
print('=='*10,'RÁDIO DO PAPAI','=='*10)
radio_do_papai = Radio(ligado=False, cor='preto', faixa='AM', peso=5, altura=6, estacao=99.1, volume=30)

radio_do_papai.volume_max=65
print(radio_do_papai)

radio_do_papai.ligar()
radio_do_papai.mudar_faixa('FM')
radio_do_papai.aumentar_volume()
radio_do_papai.passar_volume(101)