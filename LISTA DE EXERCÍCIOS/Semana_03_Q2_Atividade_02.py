class Ponto2D():
    #Atributos
    X = None #Coordenada X
    Y = None #Coordenada Y

    #construtor
    def __init__(self, X=0, Y=0):
        self.X = X
        self.Y = Y

    #Método
    def EIgual(self,ponto_a=0 ,ponto_b=0):
        if ponto_a == ponto_b:
            return True
        else:
            return False


Ponto_x = Ponto2D()
print(Ponto_x.EIgual())
Ponto_y = Ponto2D()
print(Ponto_y.EIgual(1,6))