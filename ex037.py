print("======"  "DESAFIO 108" "======")
from utilidadesCeV import moeda

p = float(input("Digite o preço R$"))
print(f"A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"Aumetando 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.aumentar(p, 10))}")
print(f"Diminuindo 13% de {moeda.moeda(p)} é {moeda.moeda(moeda.diminuir(p, 13))}")