print("======"  "DESAFIO 83" "======")
n = str(input("Digite uma expressão: "))
p = []
for s in n:
    if s == "(":
        p.append("(")
    elif s == ")":
        if len(p) > 0:
            p.pop()
        else:
            p.append(")")
            break
if len(p) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está inválida!")