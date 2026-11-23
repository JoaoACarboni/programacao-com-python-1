class Aluno:
    # Método construtor
    def __init__(self, nome, idade, curso, nota):
        self.nome = nome # Atributo
        self.idade = idade # Atributo
        self.curso = curso # Atributo
        self.nota = nota
    def apresentar(self):
        print(f"Olá! meu nome é {self.nome} tenho {self.idade} e curso {self.curso}")
    def verificarAprovacao(self):
        if self.nota > 60:
            print(f"O aluno {self.nome} foi aprovado com a nota de {self.nota}")
        else:
             print(f"O aluno {self.nome} foi reprovado com a nota de {self.nota}")
# Instanciar
aluno1 = Aluno("Fernando", 15, "IA", 80)
aluno2 = Aluno("Veroneze", 15, "IA", 55)
aluno2.apresentar()
aluno1.apresentar()
aluno1.verificarAprovacao()