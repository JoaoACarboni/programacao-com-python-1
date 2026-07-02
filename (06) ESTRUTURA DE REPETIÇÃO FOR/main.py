# ESTRUTURA DE REPETIÇÃO (FOR)
# for (variável) in (sequência)
'''
for c in range(0, 11):
    print(c)
'''
# range(início, fim, passo)

inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))
passo = int(input("Digite o passo: "))

for c in range(inicio, fim, passo):
    print(c)
print("FIM")