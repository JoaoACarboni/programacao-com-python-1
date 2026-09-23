personagens = []

def criar_personagem():
    nome = input("Digite o nome do seu personagem:")
    classe = input("Digite a classe do seu personagem:")
    nivel = int(input("Digite o nível do seu personagem:"))
    
    personagem = {
        "nome": nome,
        "classe": classe,
        "nivel": nivel
    }
    personagens.append(personagem)
    
    print("PERSONAGEM CRIADO")
    print("Nome: ", personagem["nome"])
    print("Classe: ", personagem["classe"])
    print("Nível: ", personagem["nivel"])

criar_personagem()
criar_personagem()
criar_personagem() # A gente pode chamar quantas vezes quiser