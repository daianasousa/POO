class Televisão:
    ligada = True or False
    canal = None
    volume = None
    volume_min = None
    volume_max = None

    def __init__(self, ligada=False, canal=2, canal_min=2, canal_max=99, volume_min=0, volume_max=100):
        self.ligada = ligada
        self.canal = canal
        self.canal_min = canal_min
        self.canal_max = canal_max
        self.volume_min = volume_min
        self.volume_max = volume_max

    def ligar(self):
        self.ligada = True
        self.volume = 0
        print(f'A TV está ligada e o volume está em {self.volume}.')

    def desligar(self):
        self.ligada = False
        print('A TV está desligada.')

    def mudar_canal(self, valor):
        if self.ligada == True:
            if valor > self.canal_max:
                print('Você passou do canal máximo permitido da TV.')
            elif valor < self.canal_min:
                print('Você passou do canal minimo permitido pela sua TV.')

            else:
                self.canal = valor
                print(f'Canal: {self.canal}')

    def aumentar_canal(self):
        if self.ligada == True:
            self.canal += 1
            if self.canal > self.canal_max:
                print('O canal passou do limite permitido.')
            print(f'Canal: {self.canal}')

    def diminuir_canal(self):
        if self.ligada == True:
            self.canal -= 1
            if self.canal < self.canal_min:
                print('O canal passou do minimo permitido pela TV.')
            print(f'Canal: {self.canal}')

    def aumentar_volume(self, volume):
        if self.ligada == True:
            volume += 1
            if volume > self.volume_max:
                print('Você passou do volume máximo permitido da sua TV.')
            print(f'volume: {volume}')

    def diminuir_volume(self, volume):
        if self.ligada == True:
            volume -= 1
            if volume < self.volume_min:
                print('Você passou do volume minimo permitido da sua TV.')
            print(f'volume: {volume}')


print('#=' * 10, 'TV DA SALA', '#=' * 11) 
tv_da_sala = Televisão()
tv_da_sala.ligar()
tv_da_sala.mudar_canal(7)
tv_da_sala.aumentar_volume(10)
for sala in range(0, 11):
    sala *= 2
tv_da_sala.aumentar_volume(sala)
tv_da_sala.mudar_canal(120)
for tv in range(0,21):
    tv -= 15
tv_da_sala.diminuir_volume(tv)
tv_da_sala.desligar()

print('')

print('#=' * 10, 'TV DO QUARTO', '#=' * 10)
tv_do_quarto = Televisão()
tv_do_quarto.ligar()
tv_do_quarto.mudar_canal(13)
tv_do_quarto.aumentar_volume(50)
tv_do_quarto.diminuir_canal()
for quarto in range(0, 51):
    quarto -= 3
tv_do_quarto.diminuir_volume(quarto)
tv_do_quarto.desligar()
tv_do_quarto.aumentar_canal()
tv_do_quarto.aumentar_canal()

