class Folha:
    def __init__(self, valor: str) -> None:
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

class nodo:
    def __init__(self) -> None:
        self.__esquerda = None
        self.__direita = None

    @property
    def esquerda(self):
        return self.__esquerda
    
    @esquerda.setter
    def esquerda(self, valor: str):
        self.__esquerda = valor

    @property
    def direita(self):
        return self.__direita
    
    @direita.setter
    def direita(self, valor: str):
        self.__direita = valor
