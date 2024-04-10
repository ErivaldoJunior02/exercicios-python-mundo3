print("======"  "DESAFIO 95" "======")
time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador["nome"] = str(input("Nome: "))
    qp = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()
    for c in range(1, qp + 1):
        partidas.append(int(input(f"Quantos gols na partida {c}? ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        c = str(input("Quer continuar? [S/N] "))
        if c in "SsNn":
            break
        print("ERRO: Responda apenas S ou N.")
    if c in "Nn":
        break
print("-=" * 30)
for i in jogador.keys():
    print(f"{i:<15}", end = "")
print()
print("-=" * 30)
for k, v in enumerate(time):
    print(f"{k:>3}", end="")
    for d in v.values():
        print(f"{str(d):<4} ", end = "")
    print()
print("-=" * 30)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999) para parar."))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO: Não existe jogador com o código{busca}!")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo {i+1} fez {g} gols.')
    print("-=" * 30)
print(" == VOLTE SEMPRE == ")