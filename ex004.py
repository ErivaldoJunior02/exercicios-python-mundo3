print("======"  "DESAFIO 75" "======")
n = int(input("Digite um valor: ")), int(input("Digite outro valor: ")), int(input("Digite outro valor: ")), int(input("Digite outro valor: ")),
print("Você digitou os valores {}".format(n))
print("O valor 9 apareceu {} vezes".format(n.count(9)))
if 3 in n:
   print("O valor 3 apareceu na {}ª posição".format(n.index(3)+1))
else:
    print("O valor 3 não foi digitado em nenhuma posição")
print("O números pares digitados foram ", end=" ")
for c in n:
    if c % 2 == 0:
        print(c, end=" ")
