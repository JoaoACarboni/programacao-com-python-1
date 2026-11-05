# print("Início")
# assert 1 < 0, "1 tem que ser maior do que 0"
# print("Fim")
# try:
#     idade = int(input("Digite sua idade: "))
# except: 
#     print("Digite somente números inteiros")

# try: 
#     n1 = int(input("Digite um número"))
#     n2 = int(input("Digite um número"))
#     resultado = n1 / n2
#     print("O resultado é", resultado)
# except ValueError:
#     print("Digite somente números inteiros")
# except ZeroDivisionError:
#     print("Não é possível dividir por zero!")

try:
    numero = int(input("Digite um número:"))
except ValueError:
    print("Valor inválido!")
else: # Só é executado quando o except é ignorado
    print("Número correto!")
finally: # É executado sempre, independente do valor digitado
    print("Programa finalizado!!!")
    qweqweqweqwe

