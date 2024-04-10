def aumentar(num, porcentagem, format=False):
    aumentar = num + (num * porcentagem / 100)
    return aumentar if format is False else moeda(num)

def diminuir(num, porcentagem, format=False):
    diminuir = num - (num * porcentagem / 100)
    return diminuir if format is False else moeda(num)

def dobro(num, format=False):
    num *= 2
    return num if not format else moeda(num)

def metade(num, format=False):
    num /= 2
    return num if format is False else moeda(num)

def moeda(str):
    str = f'R${str:.2f}'.replace('.', ',')
    return str

def resumo(num, aumento=0, decrescimo=0):
    print("=" * 30)
    print("       RESUMO DO VALOR")
    print("=" * 30)
    print(f"Preço analisado: R${num:.2f}")
    print(f"O dobro do preço: R${dobro(num):.2f}")
    print(f"Metade do preço: R${metade(num):.2f}")
    print(f"{aumento}% de aumento: R${num + (num * aumento / 100):.2f}")
    print(f"{decrescimo}% de redução: R${num - (num * decrescimo / 100):.2f}")