print("======"  "DESAFIO 106" "======")
def ajuda(com):
    print("==" * 50)
    print("==" * 50)
    help(com)
    print("==" * 50)
    print("==" * 50)

comando = ""
while True:
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)