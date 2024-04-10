print("======"  "DESAFIO 112" "======")
from utilidadesCeV import dado
from utilidadesCeV import moeda

p = dado.leiaDinheiro("Digite o preço: R$")
moeda.resumo(p, 35, 22)