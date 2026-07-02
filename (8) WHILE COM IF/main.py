'''
for repetidor in range(1,21):
    if repetidor % 2 == 0:
        print(repetidor)
'''
n = int(input("Digite N: "))
soma = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
        soma = soma + i
print("A soma dos pares = ", soma)
    