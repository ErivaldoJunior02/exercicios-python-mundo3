print("======"  "DESAFIO 99" "======")
from time import  sleep
def maior(* núm):
    cont = maior = 0
    print("\nAnalisando os valores passados...")
    for valor in núm:
        print(f"{valor} ", end="")
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    sleep(0.5)
    print(f"O maior valor foi {maior}")
    sleep(1)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()