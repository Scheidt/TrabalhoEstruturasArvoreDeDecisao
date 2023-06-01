class Folha:
    def __init__(self, valor: str) -> None:
        self.__valor = valor
#        self.__pai = pai

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

"""    @property
    def pai(self):
        return self.__pai
    
    @pai.setter
    def pai(self, pai):
        self.__pai = pai"""

class Nodo:
    def __init__(self, pergunta: str) -> None:
        self.__pergunta = pergunta
        self.__nao = None
        self.__sim = None

    @property
    def pergunta(self):
        return self.__pergunta
    
    @pergunta.setter
    def pergunta(self, pergunta: str):
        self.__pergunta = pergunta

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

    def adicionar_faltante(self, faltante: Folha):
        if self.__sim is None:
            self.__sim = faltante
        else:
            self.__nao = faltante