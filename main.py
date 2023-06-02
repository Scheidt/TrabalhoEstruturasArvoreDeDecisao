from classes import *

global raiz 
raiz = None
pontuacao = 0

class Play(Folha, Nodo):
    def __init__(self) -> None:
        self.__raiz = None
        self.__pontuacao = 0
        self.__listaInOrder = []

    def mostra_pontuacao(self):
        print (f"\n*5")
        if self.__pontuacao == 0:
            print("Ainda não acertei nenhuma vez. Jogue mais uma vez e eu certamente vou acertar!")
        else:
            print(f"Eu já acertei {self.__pontuacao} vezes. Se você jogar mais uma vez posso aumentar esse número!")

    def jogar(self):
        # Percorrer lista e se não der certo, adicionar
        pass

    def adicionar(self, pai: Nodo, caminhoPai: str):

        if self.__raiz is None:
            valCarta = input("Qual é a primeira carta a ser adicionada? ")
            self.__raiz = Folha(valCarta)
        elif isinstance(self.__raiz, Folha):
            resposta = input(f"Sua carta é {self.__raiz} ['s'/'n']? ")
            resposta = self.sanitizarEntrada(resposta, ('s', 'n'), "Sua resposta pode ser somente 's' ou 'n', por favor, tente novamente: ")
        else: 
            # Pegar valor para o novo filho, criar um nodo com o filho anterior e o novo
            # filho e colocar como filho do pai na posição caminhoPai
            filhoNovo = input("Qual era a sua carta? ")
            if caminhoPai == 's':
                filhoOriginal = pai.sim
                caminhoPai = 'sim'
            else:
                filhoOriginal = pai.nao
                caminhoPai = 'nao'
            pergunta = input(f"Insira uma pergunta de sim ou não que diferencie {filhoOriginal} de {filhoNovo}: ")
            posFilhoOriginal = input(f"E {filhoNovo} {pergunta} ['s'/'n'] ")
            posFilhoOriginal = self.sanitizarEntrada(posFilhoOriginal, ('s', 'n'), "Sua resposta pode ser somente 's' ou 'n', por favor, tente novamente: ")
            # Adicionar o filho em si

    """def adicionarDev(self, caminho: list, posFilhoVelho: str, valFilhoNovo: str, pergunta: str):
        if self.__raiz is None: # Se não houver nenhuma carta inscrita
            self.__raiz = Folha(valFilhoNovo)
        elif isinstance(self.__raiz, Folha): # Se houver somente uma carta inscrita
            filhoVelho = self.__raiz
            self.__raiz = Nodo(pergunta)
            if posFilhoVelho == 'sim':
                self.__raiz.sim = filhoVelho
            elif posFilhoVelho == 'nao':
                self.__raiz.nao = filhoVelho
            self.__raiz.adicionar_faltante(Folha(valFilhoNovo))
        # Olhar o código abaixo para verificar mudanças necessárias
        else:
            nodo = self.__raiz
            for passo in caminho[0, -2]: # Percorre a árvore com o caminho dado até o pai do futuro nodo
                nodo = nodo.passo
            filhoVelho = nodo.caminho[-1] # Pega a folha que será adicionada no novo nodo
            if posFilhoVelho == 'sim':
                nodo.caminho[-1] = Nodo(pergunta, filhoVelho, Folha(valFilhoNovo))
            elif posFilhoVelho == 'nao':
                nodo.caminho[-1] = Nodo(pergunta, Folha(valFilhoNovo), filhoVelho)"""

    def sanitizarEntrada(self, entrada: str, possibilidades: tuple, mensagem: str):
        while not entrada in possibilidades:
            entrada = input(mensagem)
        return entrada
           
    def inserir(self, pai, membroNovo):
        # Ver se o sim é uma folha e se não for, colocar no não
        # ACHO QUE NÃO CONSEGUE ADICIONAR FOLHAS NA DIREITA (pai.nao)
        if isinstance(pai.sim, Folha): # Se o filho sim for uma folha, seguir pelo filho da direita
            if pai.nao is None:
                pai.nao = membroNovo
            else:
                self.inserir(pai.nao, membroNovo)
        elif isinstance(pai.sim, Nodo):
            self.inserir(pai.sim, membroNovo)
        elif pai.sim is None:
            pai.sim = membroNovo
        else:
            raise Exception("Erro ao inserir filho em árvore")

    def carregar(self):
        # Carregar uma lista feita pelo inOrder a árvore em si
        # Pegar a lista do disco e colocar no self.__listaInOrder
        self.__raiz = self.__listaInOrder.pop(0)
        for membro in self.__listaInOrder:
            self.inserir(self.__raiz, membro)

    def salvar(self):
        self.inOrder
        # Colocar as funções de permanência para salvar self.__listaInOrder
        pass

    def inOrder(self, membArvore: Nodo or Folha): # Adaptei essa função do código da árvore AVL do trabalhinho. Eu NÃO pensei nisso.
        self.__listaInOrder.append(membArvore)
        if isinstance(membArvore, Folha):
            pass
        else:
            self.inOrder(membArvore.sim)
            self.inOrder(membArvore.nao)
        




# Código legado.
def jogar():
    atual = raiz
    anterior = None
    while isinstance(atual, Nodo):
        print(atual.pergunta)
        resposta = input("Responda Sim('s') ou Não('n'): ").lower()
        while resposta not in ('s', 'n'):
            resposta = input("A resposta pode ser somente 's' ou 'n', por favor, insira novamente: ").lower()
        anterior = atual
        if resposta == 's':
            atual = atual.sim
        else:
            resposta = resposta.nao
    print (f"Sua carta é {atual.valor}?") # TRABALHAR AQUI
    if not anterior is None:
        caminho = resposta
    resposta = input("Responda Sim ('s') ou Não ('n'): ").lower()
    while resposta not in ('s', 'n'):
        resposta = input("A resposta pode ser somente 's' ou 'n', por favor, insira novamente: ").lower()
    if resposta == 's':
        print("Eba! Mais uma resposta certa!")
        pontuacao += 1
        print (f"Tenho {pontuacao} acerto(s)")
    else:
        if anterior is None:
            adicionar(None, None, atual)
        adicionar(anterior, caminho,  atual)

def adicionar(pai: Nodo, caminho: str, filho1: Folha):
    global raiz
    novo = input("Qual era a sua carta? ")
    pergunta = input(f"O que diferencia {filho1.valor} de {novo}: ")
    posFilho1 = input(f"E {filho1.valor} {pergunta}?\n ['s'/'n'] ").lower()
    while not posFilho1 in ('s', 'n'):
        posFilho1 = input("A resposta pode ser somente 's' ou 'n'. Por favor, insira novamente: ").lower()
    if posFilho1 == 's':
        if pai is None:
            raiz = Nodo(pergunta, filho1, Folha(novo))
        else:
            pai.caminho = Nodo(pergunta, filho1, Folha(novo))
    else:
        if pai is None:
            raiz = Nodo(pergunta, Folha(novo), filho1)
        else:
            pai.caminho = Nodo(pergunta, Folha(novo), filho1)


raiz = Folha(input("Insira um valor para a primeira carta: "))

while True:
    jogar()

