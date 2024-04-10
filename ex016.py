print("======"  "DESAFIO 87" "======")
matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
somco = 0
msl = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l , c}]: "))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    somco += matriz[l][2]
    if matriz[1][0] == 0:
        msl = matriz[1][0]
    if matriz[1][1] > msl:
        msl = matriz[1][1]
    if matriz[1][2] > msl:
        msl = matriz[1][2]
print("-=" * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[ {matriz[l][c]:^5} ]", end="")
    print()
print("-=" * 30)
print(f"A soma dos valores pares é {pares}.")
print(f"A soma dos valores da primeira coluna é {somco}.")
print(f"O maior valor da segunda linha é {msl}.")