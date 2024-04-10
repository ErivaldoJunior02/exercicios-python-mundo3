print("======"  "DESAFIO 81" "======")
l = []
while True:
    l.append(int(input("Digite um valor: ")))
    c = str(input("Quer continuar? [S/N] "))
    if c in "Nn":
        break
l.sort(reverse=True)
print("-=" * 30)
print(f"Você digitou {len(l)} elementos.")
print(f"O valores em ordem decrescente são {l}")
if 5 in l:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não faz parte da lista!")
