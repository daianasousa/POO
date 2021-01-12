class Pessoa():
    nome = None
    idade = None
    peso = None
    altura = None
    sexo = 'm' or 'f'
    estado = 'vivo'
    estado_civil = 'solteiro'
    conjuge = None

    def __init__(self, nome, idade, peso, altura, sexo, estado='vivo', estado_civil='solteiro', conjuge='sem nome'):
        self.nome = nome
        self.__idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.__estado = estado
        self.__estado_civil = estado_civil
        self.conjuge = conjuge

    @property
    def idade(self):
        return self.__idade  
    
    @idade.setter
    def idade(self, idade):
        a = self.__idade
        b = idade
        if self.__estado == 'morto(a)':
            print(f'{self.nome} está morto.')
        elif a == b:
            self.__idade = idade
            print(f'A idade de {self.nome} é {self.__idade}.')
        else:
            print('Sem Permissão')    
    
    def envelhecer(self):
        if self.__estado != 'Morto':
            self.__idade += 1
            if self.__idade < 21:
                self.altura += 5
        print(f'{self.nome} está com {self.__idade} anos e {self.altura} cm de altura')

    def engordar(self, valor):
        if self.__estado == 'Morto':
            print(f'Operção não realizada. {self.nome} está morta')
        else:
            self.peso += valor
            print(f'O Peso atual é de {self.peso} Kg')

    def emagrecer(self, valor):
        if self.__estado != 'Morto':
            self.peso -= valor
        print(f'A Pessoa emagreceu {valor} Kg e seu peso atua é de {self.peso} Kg')
    
    def crescer(self, valor):
        if self.__estado != 'Morto':
            if self.idade <= 21:
                self.altura += valor
                print(f'A altura atual e de {self.altura} cm')
            else:
                print(f'{self.nome} não pode mais crescer pois está com 21 anos ou mais')

    def casar(self, nome_conjuge):
        if self.__estado_civil == 'casado(a)':
            print(f'Casamento não realizado. {self.nome} está casado')
        else:
            self.estado_civil = "casado(a)"
            self.conjuge = nome_conjuge
            if self.__estado == "morto(a)":
                print(f"Casamento não realizado. {self.nome} está morto.")
                
            elif self.conjuge == "Maria" or self.conjuge == "Carlos" or self.conjuge == "João":
                print(f"Casamento não permitido. {self.conjuge} é de menor.")
                
            else:
                print(f"{self.nome} está casado com {self.conjuge}.")

    
    def morrer(self):
        self.__estado = 'morto'
        print(f'{self.nome} morreu')

#OBJETOS
maria = Pessoa("Maria", 5, 20, 100, "F")
maria.idade = 10
maria.envelhecer()
maria.morrer()
maria = Pessoa("Maria", 5, 20, 100, "F", "Morto")
maria.engordar(5)

print("=="*30)

joão = Pessoa("João", 12, 40, 140, "M")
joão.idade = 50

print("=="*30)

pedro = Pessoa("Pedro", 22, 65, 170, "M")
pedro.crescer(2)
pedro.casar("Maria")
pedro.casar("Julia")
pedro = Pessoa("Pedro", 22, 65, 170, "M", "vivo","casado(a)")
pedro.casar("bia")
pedro.morrer()
pedro = Pessoa("Pedro", 22, 65, 170, "M", "morto(a)")
pedro.casar("Bia")
pedro.idade = 22


print("=="*30)

bia = Pessoa("Bia", 18, 55, 160, "F")
bia.casar("Carlos")
bia.casar("Jonas")
bia.morrer()

print("=="*30)
julia = Pessoa("Julia", 30, 65, 170, "F")
cadu = Pessoa("Carlos", 2, 11, 80, "M")

print("=="*30)
jonas = Pessoa("Jonas", 34, 70, 180, "M")
jonas.casar("Júlia")