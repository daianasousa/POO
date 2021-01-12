class Carro:
    #ATRIBUTOS
    nome = None
    ano = None
    cor = None
    veloc_max = None
    veloc_atual = None
    estado = None

    #METODOS
    def ligar(self, estado):
        if self.estado == 'ligar':
            return 'ligar'

    def desligar(self, estado):
        if self.estado == 'desligar':
            return 'desligado'

    def acelerar(self,valor, estado):
        if valor == 0:
            if self.estado == 'desligado':
                return 'Carro desligado'
        
        elif self.estado == 'ligado':
            self.veloc_atual = valor
            if self.veloc_atual > self.veloc_max:
                return f'Passou do limite de {self.veloc_max} '

            else:
                return self.veloc_atual


    def parar(self, estado,  veloc_atual):
        if self.estado == 'parar':
            self.veloc_atual = 0
            if self.veloc_atual == 0:
                return 'Carro Parado'
#OBJETO_1
fusca = Carro()
fusca.nome = 'fusca'
fusca.ano = 1965
fusca.cor = 'preto'
fusca.veloc_max = 80
fusca.veloc_atual = 20
fusca.estado = 'ligado'
#OBJETO_2
ferrari_sr2000 = Carro()
ferrari_sr2000.nome = 'ferrari_sr2000'
ferrari_sr2000.ano = 2014
ferrari_sr2000.cor = 'vermelho'
ferrari_sr2000.veloc_max = 300
ferrari_sr2000.veloc_atual = 0
ferrari_sr2000.estado = 'desligado'

fusca.acelerar(40, fusca.estado)
print(f'Velocidade atual do fusca e {fusca.veloc_atual} km/h')
ferrari_sr2000.acelerar(200, ferrari_sr2000.estado)
print(f'Velocidade atual da ferrari e {ferrari_sr2000.veloc_atual} km/h')
fusca.desligar('desligar')
print(f'Fusca {fusca.estado}')
ferrari_sr2000.ligar('ligar')
print(f'ferrari {fusca.estado}')
ferrari_sr2000.acelerar(320, ferrari_sr2000.estado)
print(f'Velocidade atual da ferrari e {ferrari_sr2000.veloc_atual} km/h')
ferrari_sr2000.parar('Pare', ferrari_sr2000.estado)
print(f'Ferrari {ferrari_sr2000.estado}')
ferrari_sr2000.desligar('desligar')
print(f'Ferrari {ferrari_sr2000.estado}')
fusca.ligar('ligar')
print(f'Fusca {fusca.estado}')
fusca.acelerar(100, fusca.estado)
print(f'{fusca.veloc_atual}')
fusca.desligar('desligar')
print(f'fusca {fusca.estado}')

    