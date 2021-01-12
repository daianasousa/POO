class Gato:
    def __init__(self, peso, idade, nome="sem nome", raça="sem raça"):
        self.__nome=nome
        self.__raça=raça
        self.__peso=peso
        self.__idade=idade
    
    @property
    def nome(self):
        return self.__nome
    def peso(self):
        return self.__peso
    def idade(self):
        return self.__idade
    def raça(self):
        return self.__raça

    def mudar_nome(self, nome):
        self.__nome = nome

    def engordar(self, peso):
        self.__peso += peso

    def envelhecer(self):
        self.__idade += 1

cat = Gato(1,1,nome="Tom", raça='Sagrado da Birmânia')
print(f'Nome: {cat.nome}\nPeso: {cat.peso()}\nIdade: {cat.idade()}\nRaça: {cat.raça()}')
cat.engordar(5)
cat.envelhecer()
cat.mudar_nome('Mimi')
print()
print(f'Nome: {cat.nome}\nPeso: {cat.peso()}\nIdade: {cat.idade()}\nRaça: {cat.raça()}')
print()

selvagem = Gato(2,1,nome="Tom", raça='Persa')
print(f'Nome: {selvagem.nome}\nPeso: {selvagem.peso()}\nIdade: {selvagem.idade()}\nRaça: {selvagem.raça()}')
selvagem.engordar(6)
selvagem.envelhecer()
selvagem.mudar_nome("Poo")
print()
print(f'Nome: {selvagem.nome}\nPeso: {selvagem.peso()}\nIdade: {selvagem.idade()}\nRaça: {selvagem.raça()}')