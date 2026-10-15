# def cadastrar_usuario(nome, idade, cidade="Não informado"):
#     print(f"Cadastro: {nome}, {idade}, {cidade}")

# cadastrar_usuario(idade=18, nome = "Joao", cidade="Amoreira")

def mostrar_nome():
    nome = "Joao" # Variável local
    return nome
# print(nome) - não funciona
print(mostrar_nome()) 

numero = 10 # Variável global
def calculo():
    global numero # Indica que quero usar a global
    numero = 20 # Cria uma NOVA variável local
calculo()
print(numero)