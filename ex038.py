print("======"  "DESAFIO 109" "======")
from utilidadesCeV import moeda

p = float(input("Digite o preço R$"))
print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}")
print(f"Aumetando 10% de {moeda.moeda(p)} é {moeda.aumentar(p, 10, True)}")
print(f"Diminuindo 13% de {moeda.moeda(p)} é {moeda.diminuir(p, 13, True)}")