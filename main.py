from classes import *
import pickle

global raiz 
raiz = None
pontuacao = 0

class Play(Folha, Nodo):
    def __init__(self) -> None:
        self.__raiz = None
        self.__pontuacao = 0
        self.__listaInOrder = []

    def menu(self): # FEITO
        switch = {'1': self.mostra_pontuacao,
                  '2': self.jogar,
                  '3': self.salvar,
                  '4': self.carregar,
                  '5': self.printarArvore} # DEVTOOL
        while True:
            print("\n"*3)
            print("Eu sou o Akinor, uma versão livre de copyright de algum outro programa. Sei todas as cartas de Clash Royale. Quer testar meus conhecimentos?\n")
            print("1: Mostrar pontuação")
            print("2: Jogar")
            print("3: Salvar dados para o disco")
            print("4: Carregar dados do disco")
            opcao = input("Insira a opção desejada: ")
            opcao = self.sanitizarEntrada(opcao, ('1', '2', '3', '4', '5'), "Você deve selecionar um número entre 1 e 4")
            switch[opcao]()

    def mostra_pontuacao(self): # FEITO
        print ("\n"*5)
        if self.__pontuacao == 0:
            print("Ainda não acertei nenhuma vez. Jogue mais uma vez e eu certamente vou acertar!")
        elif self.__pontuacao == 1:
            print("Acertei somente uma vez. Jogue mais algumas partidas pra eu aumentar esse número")
        else:
            print(f"Eu já acertei {self.__pontuacao} vezes. Se você jogar mais uma vez posso aumentar esse número!")

    def jogar(self):
        if isinstance(self.__raiz, Nodo): # Se houver ao menos uma pergunta
            atual = self.__raiz
            while isinstance(atual, Nodo):
                print(f"Sua carta {atual.pergunta}")
                resposta = input(f"['s'/'n']? ")
                resposta = self.sanitizarEntrada(resposta, ('s', 'n'), "Sua resposta pode ser somente 's' ou 'n', por favor, tente novamente: ")
                pai = atual
                if resposta == 's':
                    atual = atual.sim
                else:
                    atual = atual.nao
            print (f"Sua carta é {atual.valor}? ['s'/'n']")
            acertou = input(f"['s'/'n']? ")
            acertou = self.sanitizarEntrada(acertou, ('s', 'n'), "Sua resposta pode ser somente 's' ou 'n', por favor, tente novamente: ")
            if acertou == 's':
                print("\n"*5)
                print ("Eba! Acertei mais uma vez")
                self.__pontuacao += 1
                return
            else:
                self.adicionar(pai, resposta)
        if self.__raiz is None: # Se não houver carta inscrita
            self.adicionar(None, None)
            return
        elif isinstance(self.__raiz, Folha): # Se houver somente uma carta inscrita
            resposta = input(f"Sua carta é {self.__raiz.valor} ['s'/'n']? ")
            resposta = self.sanitizarEntrada(resposta, ('s', 'n'), "Sua resposta pode ser somente 's' ou 'n', por favor, tente novamente: ")
            if resposta == 's':
                print("\n"*5)
                print ("Eba! Acertei mais uma vez")
                self.__pontuacao += 1
                return
            else:
                self.adicionar(None, None)
            return
                        

    def adicionar(self, pai: Nodo, caminhoPai: str):

        if self.__raiz is None: # Se não houver nenhuma carta inscrita
            valFilhoNovo = input("Qual é a primeira carta a ser adicionada? ")
            self.__raiz = Folha(valFilhoNovo)
            return
        elif isinstance(self.__raiz, Folha): # Se houver somente uma carta inscrita
            valFilhoNovo = input("Qual era a sua carta? ")
            filhoOriginal = self.__raiz
            pergunta = input(f"Insira uma pergunta de sim ou não que diferencie {filhoOriginal.valor} de {valFilhoNovo}: ")
            posFilhoOriginal = input(f"E {filhoOriginal.valor} {pergunta} ['s'/'n'] ")
            posFilhoOriginal = self.sanitizarEntrada(posFilhoOriginal, ('s', 'n'), "Sua resposta pode ser somente 's' ou 'n', por favor, tente novamente: ")
            self.__raiz = Nodo(pergunta)
            if posFilhoOriginal == 's':
                self.__raiz.sim = filhoOriginal
            else:
                self.__raiz.nao = filhoOriginal
            self.__raiz.adicionar_faltante(Folha(valFilhoNovo))
        else: # Se houver mais de uma carta inscrita
            valFilhoNovo = input("Qual era a sua carta? ")
            if caminhoPai == 's': # Pega o filho original e deleta ele do Nodo
                filhoOriginal = pai.sim
                pai.sim = None
            else:
                filhoOriginal = pai.nao
                pai.nao = None
            pergunta = input(f"Insira uma pergunta de sim ou não que diferencie {filhoOriginal.valor} de {valFilhoNovo}: ")
            posFilhoOriginal = input(f"E {filhoOriginal.valor} {pergunta} ['s'/'n'] ")
            posFilhoOriginal = self.sanitizarEntrada(posFilhoOriginal, ('s', 'n'), "Sua resposta pode ser somente 's' ou 'n', por favor, tente novamente: ")
            novoPai = Nodo(pergunta)
            pai.adicionar_faltante(novoPai)
            if posFilhoOriginal == 's':
                novoPai.sim = filhoOriginal
            else:
                novoPai.nao = filhoOriginal
            novoPai.adicionar_faltante(Folha(valFilhoNovo))


    def sanitizarEntrada(self, entrada: str, possibilidades: tuple, mensagem: str):
        while not entrada in possibilidades:
            entrada = input(mensagem)
        return entrada
           
    def inserir(self, pai, membroNovo): # Feito
        # Para melhor compreensão, imagine o 'sim' para a esquerda e o 'nao' para a direita, os comentários indicam cada cas
        # dos filhos. Por exemplo, "Folha - Nodo" indica que o filho esquerdo é uma Folha e o direito um Nodo
        if isinstance(pai.sim, Folha): # Folha - ?
            if pai.nao is None: # Folha - None
                pai.nao = membroNovo
                return True
            elif isinstance(pai.nao, Nodo): # Folha - Nodo
                sucesso = self.inserir(pai.nao, membroNovo)
                if sucesso: # Se conseguiu inserir ele sobe um True (Isso não é tão util, mas é importante se for False)
                    return True
            elif isinstance(pai.nao, Folha): # Folha - Folha
                return False
        elif isinstance(pai.sim, Nodo): # Nodo - ?
            sucesso = self.inserir(pai.sim, membroNovo)
            if sucesso:
                return True
            else: # Se, seguindo pela esquerda não encontrar um Nodo faltando um filho, a recursão entra nesse If.
                if isinstance(pai.nao, Nodo): # Nodo 'cheio' - Nodo possivelmente com espaço
                    sucesso = self.inserir(pai.nao, membroNovo) # Passa o valor pro nodo da direita e inicia recursão nele.
                    return sucesso                              # Se encontrar um slot ele vai subir como True. Se não ele passa
                                                                # pro pai um False
                elif isinstance(pai.nao, Folha): # Nodo 'cheio' - Folha
                    return False
        elif pai.sim is None: # None - ?
            pai.sim = membroNovo
            return True
        else:
            raise Exception("Erro ao inserir filho em árvore")

    def carregar(self): # FEITO
        # Carregar uma lista feita pelo inOrder a árvore em si
        # Pegar a lista do disco e colocar no self.__listaInOrder
        with open('list_data.pkl', 'rb') as file:
            self.__listaInOrder = pickle.load(file)
        self.__raiz = self.__listaInOrder.pop(0)
        for membro in self.__listaInOrder:
            self.inserir(self.__raiz, membro)

    def salvar(self): # FEITO
        self.inOrder(self.__raiz)
        with open('list_data.pkl', 'wb') as file:
            pickle.dump(self.__listaInOrder, file)
        # Colocar as funções de permanência para salvar self.__listaInOrder
        pass

    def inOrder(self, membArvore: Nodo or Folha): # Adaptei essa função do código da árvore AVL do trabalhinho. Eu NÃO pensei nisso.
        self.__listaInOrder.append(membArvore)
        if isinstance(membArvore, Folha):
            pass
        else:
            self.inOrder(membArvore.sim)
            self.inOrder(membArvore.nao)

    def printarArvore(self): # FEITO
        self.inOrder(self.__raiz)
        for i in self.__listaInOrder:
            if isinstance(i, Nodo):
                print (i.pergunta)
            else:
                print(i.valor)
        

jogo = Play()
jogo.menu()