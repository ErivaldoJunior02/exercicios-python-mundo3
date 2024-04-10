print("======"  "DESAFIO 89" "======")
alunos = []
while True:
    nome = str(input("Nome: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    m = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], m])
    c = str(input("Quer continuar? [S/N]"))
    if c in "Nn":
        break
print("-=" * 30)
print(f'{"No.":>4} {"NOME":<10} {"MÉDIA":>8}')
for i, a in enumerate(alunos):
    print(f"{i:<4} {a[0]:<10} {a[2]:>8.1f}")
while True:
    print("-=" * 30)
    opc = int(input("Mostrar nota de que aluno? (999) para parar. "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if opc <= len(alunos) - 1:
        print(f"As notas do aluno {alunos[opc][0]} foram {alunos[opc][1]}")