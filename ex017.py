print("======"  "DESAFIO 88" "======")
from random import randint
from time import sleep
jogos = int(input("Quantos jogos vocÊ quer que eu sorteie? "))
cont = 0
jogada = []
print(f"=-=-=- SORTEANDO {jogos} JOGOS -=-=-=")
for c in range(1, jogos + 1):
    while True:
        n = randint(1, 60)
        if n not in jogada:
            jogada.append(n)
            cont += 1
        if cont >= 6:
            break
    jogada.sort()
    print(f"Jogo {c}: {jogada}")
    jogada.clear()
    cont = 0
    sleep(1)
print("=-=-=- < BOA SORTE > -=-=-=")