from classes import *

raiz = None
pontuacao = 0

def jogar():
    atual = raiz
    anterior = None
    while isinstance(atual, Nodo):
        print(atual.pergunta)
        resposta = input("Responda Sim(s) ou Não(n)").lower()
        while resposta not in ('s', 'n'):
            resposta = input("A resposta pode ser somente 's' ou 'n', por favor, insira novamente").lower()
        anterior = atual
        if resposta == 's':
            atual = atual.sim
        else:
            resposta = resposta.nao
    print (f"Sua carta é {atual.valor}?")
    caminho = resposta
    resposta = input("Responda Sim ('s') ou Não ('n')").lower()
    while resposta not in ('s', 'n'):
        resposta = input("A resposta pode ser somente 's' ou 'n', por favor, insira novamente").lower()
    if resposta == 's':
        print("Eba! Mais uma resposta certa!")
        pontuacao += 1
        print (f"Tenho {pontuacao} acerto(s)")
    else:
        adicionar(anterior, caminho,  atual)

def adicionar(pai: Nodo, caminho: str, filho1: Folha):
    novo = input("Qual era a sua carta?")
    pergunta = input(f"O que diferencia {filho1.valor} de {novo}")
    posFilho1 = input(f"E {filho1.valor} {pergunta}? ['s'/'n']").lower()
    while not posFilho1 in ('s', 'n'):
        posFilho1 = input("A resposta pode ser somente 's' ou 'n'. Por favor, insira novamente").lower()
    if posFilho1 == 's':
        pai.caminho = Nodo(pergunta, filho1, Folha(novo))
    else:
        pai.caminho = Nodo(pergunta, Folha(novo), filho1)


raiz = Folha(input("Insira um valor para a primeira carta"))
while True:
    jogar()

