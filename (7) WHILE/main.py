'''
n = 100
while n > 0: #Enquanto N for maior do que zero faça:
    print(n)
    n -= 1
    # n = n -1 (É A MESMA COISA)
print("LANÇAR!")
'''

# Pedir senha até acertar
usuario_correto = "joao antonio"
senha_correta = "123"
usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

while senha != senha_correta or usuario != usuario_correto:
    print("USUÁRIO OU SENHA INCORRETO. TENTE NOVAMENTE!")
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

print("ACESSO LIBERADO!")
    




