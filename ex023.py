print("======"  "DESAFIO 94" "======")
pessoas = {}
cadastro = []
pec = 0
med = 0
lm = []
while True:
    pessoas['nome'] = str(input("Nome: "))
    pessoas['sexo'] = str(input("Sexo: [F/M] "))
    while pessoas['sexo'] not in "MmFf":
        print("ERRO: Por favor, digite apenas F ou M.")
        pessoas['sexo'] = str(input("Sexo: [F/M] "))
    pessoas['idade'] = int(input("Idade: "))
    cadastro.append(pessoas.copy())
    pec += 1
    med += pessoas['idade']
    if pessoas['sexo'] in "Ff":
        lm.append(pessoas['nome'])
    pessoas.clear()
    c = str(input("Quer continuar? [S/N] "))
    while c not in "SsNn":
        print("ERRO: Responda apenas S ou N.")
        c = str(input("Quer continuar? [S/N] "))
    if c in "Nn":
        break
medf = med / pec
print("-=" * 30)
print(f"Você cadastrou {pec} pessoas.")
print(f"A média de idade cadastrada é de {medf}.")
print(f"A lista de mulheres é {lm}.")
print("Pessoas acima da média:")
for p in cadastro:
    if p["idade"] > medf:
        for k, v in p.items():
            print(f"{k} = {v}", end=" ")
print("\nENCERRADO")

