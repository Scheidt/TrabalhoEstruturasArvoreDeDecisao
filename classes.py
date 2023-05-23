class Folha:
    def __init__(self, valor: str, pai) -> None:
        self.__valor = valor
        self.__pai = pai

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

    @property
    def pai(self):
        return self.__pai
    
    @pai.setter
    def pai(self, pai):
        self.__pai = pai

class Nodo:
    def __init__(self) -> None:
        self.__nao = None
        self.__sim = None

    @property
    def nao(self):
        return self.__nao
    
    @nao.setter
    def nao(self, valor: str):
        self.__nao = valor

    @property
    def sim(self):
        return self.__sim
    
    @sim.setter
    def sim(self, valor: str):
        self.__sim = valor
