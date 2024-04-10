print("======"  "DESAFIO 104" "======")
def leiaint(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("ERRO, por favor digite um número inteiro!")
        if ok:
            break
    return valor


n = leiaint("Digite um número: ")
print(f"Você acabou de digitar o número {n}.")