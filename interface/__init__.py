def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO: por favor digite um número válido.")
        except (KeyboardInterrupt):
            print("Usuário pregeriu não digitar esse número.")
            return 0
        else:
            return n

def linha(tam = 42):
    return "-" * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print(linha())
    opc = leiaint("Sua opção: ")
    return opc