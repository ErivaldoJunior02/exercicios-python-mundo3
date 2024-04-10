print("======"  "DESAFIO 84" "======")
temp = []
pessoas = []
cadastro = 0
maipe = menpe = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maipe = menpe = temp[1]
    else:
        if temp[1] > maipe:
            maipe = temp[1]
        if temp[1] < menpe:
            menpe = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    c = str(input("Quer continuar? [S/N]"))
    if c in "Nn":
        break
print("-=" * 30)
print(f"Ao todo você cadastrou {len(pessoas)} pessoas.")
print(f"\nO maior peso foi de {maipe}Kg. Peso de", end=" ")
for p in pessoas:
    if p[1] == maipe:
        print(f"{[p[0]]}", end = " ")
print(f"\nO menor peso foi de {menpe}Kg. Peso de", end=" ")
for p in pessoas:
    if p[1] == menpe:
        print(f"{[p[0]]}", end=" ")