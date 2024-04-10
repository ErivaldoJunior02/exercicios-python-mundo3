print("======"  "DESAFIO 77" "======")
palavras = ("aprender", "programar", "linguagem", "python",
            "curso", "video", "estudar", "praticar",
            "trabalar", "mercado", "programador", "futuro")
for p in palavras:
    print("\n Na palavra {} temos".format(p.upper()), end = " ")
    for letra in p:
        if letra.lower() in "AaEeIiOoUu":
            print(letra, end = " ")

