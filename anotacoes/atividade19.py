##fute
jogador = {}
partidas = [] jogador['nome'] = input('Nome do jogador: ') jogos = int(input(f'Quantas partidas
{jogador["nome"]} jogou?'))
for i in range(jogos):
partidas.append(int(input(f'Quantos gols na partida {i + 1}? ')))
jogador['gols'] = partidas
jogador['total'] = sum(partidas)
print(jogador)