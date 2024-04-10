print("======"  "DESAFIO 115" "======")
import interface
from time import sleep

while True:
    resposta = interface.menu(["Ver pessoas cadastradas", "Cadastrar pessoas","Sair do sistema"])
    if resposta == 1:
        print("opção 1")
    elif resposta == 2:
        print("opção 2")
    elif resposta == 3:
        interface.cabecalho("Saindo do sistema... Até logo!")
        break
    else:
        print("Digite uma opção válida")
    sleep(1.3)

