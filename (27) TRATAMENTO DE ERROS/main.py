# print("Início")

# assert 2 < 1, "2 tem que ser maior do que 1"

# print("Fim")

try:
    idade = int(input("Digite sua idade: "))
    print("Sua idade é", idade)
except:
    print("Digite um número!")

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(resultado)
except ValueError:
    print("DIGITE UM NÚMERO INTEIRO!!")
except ZeroDivisionError:
    print("NÃO EXISTE DIVISÃO POR ZERO")
