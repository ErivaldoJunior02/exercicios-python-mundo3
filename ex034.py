print("======"  "DESAFIO 105" "======")
def notas(*n, sit=False):
    """
    -> FUnção para analisar notas e situações de varios alunos.
    :param n: Uma ou mais notas de alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = {}
    r["total"] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = "BOA"
        elif r["media"] >= 5:
            r['situação'] = "RAZOÁVEL"
        else:
            r['situação'] = "RUIM"
    return r

resp = notas(5.8, 2.5, 1.5, sit=True)
print(resp)
