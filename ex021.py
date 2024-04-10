print("======"  "DESAFIO 92" "======")
from datetime import date
ctps = {}
ctps["nome"] = str(input("Nome: "))
ano = int(input("Ano de nascimento: "))
ctps["idade"] = date.today().year - ano
ctps["carteira"] = int(input("Número da carteira de trabalho (0 não tem): "))
if ctps["carteira"] != 0:
    ctps["contratacao"] = int(input("Ano de contratação: "))
    ctps["salario"] = float(input("Salário: R$"))
    ctps["aposentadoria"] = ctps['idade'] + ((ctps["contratacao"] + 35) - date.today().year)
print("-=" * 30)
if ctps["carteira"] != 0:
    print(f"Nome: {ctps['nome']}")
    print(f"Idade: {ctps['idade']}")
    print(f"CTPS: {ctps['carteira']}")
    print(f"Contratação: {ctps['contratacao']}")
    print(f"Salário: R${ctps['salario']}")
    print(f"Aposentadoria: {ctps['aposentadoria']}")
if ctps["carteira"] == 0:
    print(f"Nome: {ctps['nome']}")
    print(f"Idade: {ctps['idade']}")
    print(f"CTPS: {ctps['carteira']}")