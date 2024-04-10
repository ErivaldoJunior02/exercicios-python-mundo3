print("======"  "DESAFIO 101" "======")
from datetime import date
def voto(ano=0):
    idade = date.today().year - ano
    if idade < 16:
        return f"Você tem {idade} anos, VOTO NEGADO!"
    elif idade < 18 or idade > 65:
        return f"Você tem {idade} anos, VOTO OPCIONAL!"
    else:
        return f"Você tem {idade} anos, VOTO OBRIGATÓRIO!"


nasc = int(input("Ano de nascimento: "))
print(voto(nasc))

