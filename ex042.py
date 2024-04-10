print("======"  "DESAFIO 113" "======")
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print("ERRO: por favor, digite um número inteiro válido.")
            continue
        else:
            return n


n = leiaint("Digite um número: ")
print(f"Você acabou de digitar o número {n}.")