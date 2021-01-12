class Radio:
    #Atributos
    ligado = True
    cor = None
    faixa = None
    peso = None
    altura = None
    volume = 0
    estacao = None
    volume_max = 0
    volume_min = 0

    #Construtores
    def __init__(self, ligado=False, volume_max=100, volume_min=0):
        self.ligado = ligado
        self.volume_max = volume_max
        self.volume_min = volume_min

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
        if self.volume > self.volume_max:
            print('Passou do volume máximo permitido.')
        
        elif self.volume < self.volume_min:
            print('Passou do volume minimo permitido.')
        
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
        if self.volume > self.volume_max:
            print('Passou do volume máximo permitido.')
            print(f'volume atual: {self.volume}')

    def diminuir_volume(self):
        self.volume -= 1
        if self.volume < self.volume_min:
            print('Passou do volume minimo permitido.')
        print(f'volume atual: {self.volume}')

#Objeto_1
print('=='*10,'RÁDIO DO VOVÔ','=='*10)
radio_do_vovo = Radio()
radio_do_vovo.ligado = False 
radio_do_vovo.cor = 'Preto'
radio_do_vovo.faixa = 'FM'
radio_do_vovo.peso = 1.5
radio_do_vovo.altura = 15
radio_do_vovo.volume = 25
radio_do_vovo.estacao = 101.0

radio_do_vovo.ligar()
radio_do_vovo.desligar()
radio_do_vovo.mudar_faixa('AM')
radio_do_vovo.mudar_estação(99.0)
radio_do_vovo.ligar()
radio_do_vovo.mudar_estação(99.0)
radio_do_vovo.passar_estação()
radio_do_vovo.diminuir_volume()
radio_do_vovo.desligar()
print(f'A Cor do rádio do meu avô é {radio_do_vovo.cor}')

print('')
#Objeto_2
print('=='*10,'RÁDIO DO PAPAI','=='*10)
radio_do_papai = Radio()
radio_do_papai.ligado = True
radio_do_papai.cor = 'Amarelo'
radio_do_papai.faixa = 'AM'
radio_do_papai.peso = 1.0
radio_do_papai.altura = 10
radio_do_papai.volume = 30
radio_do_papai.estacao = 94.5

radio_do_papai.ligar()
radio_do_papai.mudar_faixa('FM')
radio_do_papai.aumentar_volume()
radio_do_papai.aumentar_volume()
radio_do_papai.aumentar_volume()
radio_do_papai.mudar_estação(78.4)
radio_do_papai.passar_volume(101)
radio_do_papai.diminuir_volume()
radio_do_papai.diminuir_volume()
radio_do_papai.diminuir_volume()
radio_do_papai.passar_estação()
radio_do_papai.passar_estação()
radio_do_papai.desligar()
radio_do_papai.mudar_estação(99.9)
radio_do_papai.ligar()
print(f'A Cor do rádio do meu Pai é {radio_do_papai.cor}')