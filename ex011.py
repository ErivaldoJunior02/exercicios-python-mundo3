print("======"  "DESAFIO 82" "======")
l = []
li = []
lp = []
while True:
    n = (int(input("Digite um número: ")))
    if n % 2 == 0:
        l.append(n)
        lp.append(n)
    if n % 2 == 1:
        l.append(n)
        li.append(n)
    c = str(input("Quer continuar? [S/N] "))
    if c in "Nn":
        break
print(f"Os valores digitados foram {l}.")
print(f"Os valores ímpares são {li}.")
print(f"Os valores pares são {lp}")