print("======"  "DESAFIO 93" "======")
jogador = {}
jogador["nome"] = str(input("Nome: "))
qp = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
gols = []
sgols = 0
for c in range(1, qp + 1):
    g = int(input(f"Quantos gols na partida {c}? "))
    gols.append(g)
    sgols += g
jogador['gols'] = gols
jogador['total'] = sgols
print("-=" * 30)
print(jogador)
print("-=" * 30)
print(f"Nome: {jogador['nome']}")
print(f"Gols: {jogador['gols']}")
print(f"Total de gols: {jogador['total']}")
print("-=" * 30)
print(f"O jogador {jogador['nome']} jogou {qp} partidas.")
for g, v in enumerate(jogador['gols']):
    print(f"Na partida {g+1}, fez {v} gols.")
print(f"Total de {jogador['total']} gols")
