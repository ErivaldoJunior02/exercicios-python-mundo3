print("======"  "DESAFIO 98" "======")
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print("-=" * 20)
    print(f"Contagem de {i} a {f} de {p} em {p}")
    sleep(2)


    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end='')
            sleep(0.5)
            cont += p
        print("FIM!")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ", end='')
            sleep(0.5)
            cont -= p
        print("FIM!")

contador(0, 100, 10)
contador(10, 0, 2)
print("-=" * 20)
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)