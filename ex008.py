print("======"  "DESAFIO 79" "======")
l = []
while True:
    n = int(input("Digite um valor: "))
    if n in l:
        n = int(input("Valor já cadastrado, tente novamente: "))
    print("Valor adicionado com sucesso...")
    l.append(n)
    c = str(input("Quer continuar? [S/N] "))
    if c not in "SsNn":
        c = str(input("Favor informar se quer continuar: [S/N]"))
    if c in "Nn":
        break
l.sort()
print("=-" * 30)
print(f"Você digitou os valores {l}")
