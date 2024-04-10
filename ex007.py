print("======"  "DESAFIO 78" "======")
l = []
ma = 0
me = 0
for cont in range(0, 5):
    l.append(int(input("Digite um valor: ")))
    if cont == 0:
        ma = me = l[cont]
    else:
        if l[cont] > ma:
            ma = l[cont]
        if l[cont] < me:
            me = l[cont]
print("-=" * 30)
print(f"Você digitou os números {l}.")
print(f"O maior valor digitado foi {ma} nas posições.", end = "")
for i, v in enumerate(l):
    if v == ma:
        print(f"{i}...",end = "")
print(f"\nO menor valor digitado foi {me} nas posições.", end = "")
for i, v in enumerate(l):
    if v == me:
        print(f"{i}...", end = "")




