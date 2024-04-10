print("======"  "DESAFIO 80" "======")
l = []
for c in range(0, 5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > l[-1]:
        l.append(n)
        print("Adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(l):
            if n <= l[pos]:
                l.insert(pos, n)
                print(f"Adicionado na posição {pos} da lista...")
                break
            pos += 1
print("-=" * 30)
print(f"Os valores digitados em ordem foram{l}")


