'''
frase ="Professor João Antonio"
print("Antonio" in frase)
print("Python" in frase)
'''
alunos = ["gabriel", "gustavo", "felipe"]
nome = input("Digite um nome: ")

if nome.lower() in alunos:
    print(f"{nome} está na turma")
else:
    print(f"{nome} não está na turma")