class Folha:
    def __init__(self, valor: str) -> None:
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

class Nodo:
    def __init__(self, pergunta: str, sim = None, nao = None) -> None:
        self.__pergunta = pergunta
        self.__nao = nao
        self.__sim = sim

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
            return True
        elif self.__nao is None:
            self.__nao = faltante
            return True
        return False