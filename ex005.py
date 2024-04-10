print("======"  "DESAFIO 76" "======")
l = ("Caneta", 1.5,
     "Lápis", 1,
     "Caderno", 35,
     "Estojo", 5.6,
     "Borracha", 2,
     "Corretivo", 3.5)
print("=" * 40)
print("LISTAGEM DE PREÇOS")
print("=" * 40)
for i in range(0, len(l)):
    if i % 2 == 0:
        print("{:.<30}".format(l[i]), end = "")
    else:
        print("R${:>7.2f}".format(l[i]))
print("=" * 40)