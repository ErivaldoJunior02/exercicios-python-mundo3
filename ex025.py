print("======"  "DESAFIO 96" "======")
def área(l, c):
    print('-=' * 20)
    a = l * c
    print(f"A área de um terreno {l}m x {c}m é {a}m²")


print(" CONTROLE DE TERRENOS ")
print("-=" * 20)
v = float(input("LARGURA (m): "))
v2 = float(input("COMPRIMENTO (m): "))
área(v, v2)

