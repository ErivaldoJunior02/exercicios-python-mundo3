print("======"  "DESAFIO 100" "======")
from random import randint
from time import sleep

def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f"{n} ", end="")
        sleep(0.3)
    print("PRONTO!")

def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f"Somando os valor pares de {lista}, temos {soma}")



numeros = []
sorteia(numeros)
somapar(numeros)
