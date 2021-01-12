class Bicicleta:
    #atributos
    peso = None
    altura = None
    veloc_atual = 0
    cor = None
    aro = None
    altura_cela = 0
    calibragem_pneus = 0

    #métodos
    def pedalar(self):
        veloc_max = 15
        self.veloc_atual += 1
        if self.veloc_atual > veloc_max:
            print('Você passou da velocidade máxima permitida')

        else:
            print(f'Velocidade atual: {self.veloc_atual}') 

    
    def frear(self):
        self.veloc_atual -= 1
        veloc_min = 5
        if self.veloc_atual < veloc_min:
            print('está abaixo da velocidade permitida')
        
        else:
            print(f'Velocidade atual: {self.veloc_atual}')

    def regular_cela(self, valor):
        if self.veloc_atual == 0:
            altura_max = 12
            altura_min = 2
            self.altura_cela = valor
            if self.altura_cela > altura_max:
                print('Cela muito alta. Perigo de queda!')

            elif self.altura_cela < altura_min:
                print('Cela muito baixa para uso')

            else:
                print(f'Altura atual da cela: {self.altura_cela} cm')
        else:
            print('Pare sua bicicleta')

    def calibrar_pneus(self, valor):
        if self.veloc_atual == 0:
            calibragem_max = 45
            calibragem_min = 25
            self.calibragem_pneus = valor
            if self.calibragem_pneus > calibragem_max:
                print('Perigo!Calibgragem muito alta do permitido!')

            elif self.calibragem_pneus < calibragem_min:
                print('Bicileta com pneu seco.')

            else:
                print(f'Calibragem atual dos pneus: {self.calibragem_pneus}')

        else:
            print('Pare agora a bicicleta')

#criação de objetos
minha_bicicleta = Bicicleta()
minha_bicicleta.peso = 10
minha_bicicleta.altura = 100
minha_bicicleta.cor = 'AMARELA'
minha_bicicleta.aro = 29
minha_bicicleta.regular_cela(5)
minha_bicicleta.calibrar_pneus(25)
minha_bicicleta.pedalar()
minha_bicicleta.pedalar()
minha_bicicleta.frear()
minha_bicicleta.frear()
print(f'Cor: {minha_bicicleta.cor}')  
print(f'Aro: {minha_bicicleta.aro}')  