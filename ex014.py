print("======"  "DESAFIO 85" "======")
paim = [[], []]
for c in range(1,8):
    v = (int(input(f"Digite o {c}º valor: ")))
    if v % 2 == 0:
        paim[0].append(v)
    if v % 2 == 1:
        paim[1].append(v)
paim[0].sort()
paim[1].sort()
print("-=" * 30)
print(f"Os números pares digitados foram: {paim[0]}")
print(f"Os números ímpares digitados foram: {paim[1]}")

