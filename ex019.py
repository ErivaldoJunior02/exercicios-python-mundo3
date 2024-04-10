print("======"  "DESAFIO 90" "======")
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['media'] >= 7:
    print(f"Nome: {aluno['nome']}")
    print(f'Média: {aluno["media"]}')
    print(f'Situação: APROVADO(a)')
elif aluno['media'] < 7 and aluno["media"] >= 5:
    print(f'Nome: {aluno["nome"]}')
    print(f'Média: {aluno["media"]}')
    print('Situação: RECUPERAÇÃO')
else:
    print(f'Nome: {aluno["nome"]}')
    print(f'Média: {aluno["media"]}')
    print('Situação: REPROVADO(a)')