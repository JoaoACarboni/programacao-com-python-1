# Condicional encadeada

# Recebimento de dado
nota = float(input("Digite a nota do aluno:"))

if nota < 4:
    print('Reprovado')
elif nota < 6:
    print('Recuperação')
else:
    print('Aprovado')