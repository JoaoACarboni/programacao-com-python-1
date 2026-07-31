lista_frutas = ["Maçã", "Banana", "Laranja", "Uva", "Abacaxi"]

fruta_pesquisada = input("Digite o nome de uma fruta: ").lower()

fruta_encontrada = False

for fruta_atual in lista_frutas:

    if fruta_pesquisada in fruta_atual.lower():
        fruta_encontrada = True

if fruta_encontrada:
    print("Fruta encontrada na lista!")
else:
    print("Fruta não encontrada.")



    