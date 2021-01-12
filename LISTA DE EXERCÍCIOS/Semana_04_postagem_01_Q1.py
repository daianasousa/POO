class Televisão:
    def __init__(self, ligada=False, canal=0, canal_min=2, canal_max=99, volume_min=0, volume_max=100):
        self.__ligada = ligada
        self.__canal = canal
        self.__canal_min = canal_min
        self.__canal_max = canal_max
        self.__volume_min = volume_min
        self.__volume_max = volume_max

    @property
    def ligar(self):
        self.__ligada = True
        self.__volume = 0
        return f'A TV está ligada e o volume está em {self.__volume}.'

    def desligar(self):
        self.__ligada = False
        return 'A TV está desligada.'
    
    def mudar_canal(self, valor):
        if self.__ligada == True:
            if valor > self.__canal_max:
                print('Você passou do canal máximo permitido da TV.')
            elif valor < self.__canal_min:
                print('Você passou do canal minimo permitido pela sua TV.')

            else:
                self.__canal = valor
                print(f'Canal: {self.__canal}')

    def aumentar_canal(self, valor=1):
        if self.__ligada == True:
            self.__canal += valor
            if self.__canal > self.__canal_max:
                print('O canal passou do limite permitido')
            else:
                print(f'Canal: {self.__canal}')

    def diminuir_canal(self, valor=1):
        if self.__ligada == True:
            self.__canal -= valor
            if self.__canal < self.__canal_min:
                print('O canal passou do minimo permitido pela TV')
            else:
                print(f'Canal: {self.__canal}')

    def aumentar_volume(self, volume):
        if self.__ligada == True:
            self.__volume += volume
            if self.__volume > self.__volume_max:
                print('Você passou do volume máximo permitido da sua TV')
            else:
                print(f'volume: {self.__volume}')

    def diminuir_volume(self, volume):
        if self.__ligada == True:
            self.__volume -= volume
            if self.__volume < self.__volume_min:
                print('Você passou do volume minimo permitido da sua TV')
            else:
                print(f'volume: {self.__volume}')


print('#=' * 10, 'TV DA SALA', '#=' * 11) 
tv_da_sala = Televisão()
print(tv_da_sala.ligar)
tv_da_sala.mudar_canal(7)
tv_da_sala.aumentar_volume(10)
for sala in range(0, 11):
    sala *= 2
tv_da_sala.aumentar_volume(sala)
tv_da_sala.mudar_canal(120)
for tv in range(0,21):
    tv -= 15
tv_da_sala.diminuir_volume(tv)
tv_da_sala.aumentar_canal()
print(tv_da_sala.desligar())

print('')

print('#=' * 10, 'TV DO QUARTO', '#=' * 10)
tv_do_quarto = Televisão()
print(tv_do_quarto.ligar)
tv_do_quarto.mudar_canal(13)
tv_do_quarto.aumentar_volume(50)
tv_do_quarto.diminuir_canal()
for quarto in range(0, 51):
    quarto -= 3
tv_do_quarto.diminuir_volume(quarto)
print(tv_do_quarto.desligar())
print(tv_do_quarto.ligar)
tv_do_quarto.aumentar_canal()
tv_do_quarto.aumentar_canal()
tv_do_quarto.aumentar_volume(98)
print(tv_do_quarto.desligar())