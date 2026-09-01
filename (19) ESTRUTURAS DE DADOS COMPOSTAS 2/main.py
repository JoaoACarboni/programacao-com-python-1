# Estruturas de Dados Compostas 2 
# LISTA de LISTAS

jogos = [
    ["CS2", "ROBLOX", "RDR2"], # Jogos de PC
    ["AstroBot", "God of War", "The Last of Us"], # Jogos de PS4
    ["Halo", "Forza Horizon", "Gears of War"] # Jogos de XBOX
]
print(len(jogos)) # Quantidade de listas dentro da lista

print("Jogos por plataforma:\n")
print("Jogos de PC: ")
for jogo in jogos[0]:
    print(jogo)

print("\nJogos de PS4: ")
for jogo in jogos[1]:
    print(jogo)

print("\nJogos de XBOX: ")
for jogo in jogos[2]:
    print(jogo)