# Lista de dicionário ou dict

personagens = [
    {"nome": "Bob Esponja", "idade": 23},
    {"nome": "Thanos", "idade": 1000}
]
# print(personagens[0]["nome"])
# print(personagens[1]["nome"]) 
for persongagem in personagens:
    print("Nome:", persongagem["nome"])
    print("Idade:", persongagem["idade"])
    print("--------------------")