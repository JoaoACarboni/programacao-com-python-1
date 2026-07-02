# CALCULADORA SIMPLES

while True:
    
    op = input("Operação (+, -, *, /) ou 0 para sair: ")
    
    if op == '0':
        print("Encerrando...")
        break
    
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))

    if op == "+":
        print(n1 + n2)
    
    elif op == "-":
        print(n1 - n2)
    
    elif op == "*":
        print(n1 * n2)
    
    elif op == "/":
        print(n1 / n2)
    
    else:
        print("Operação inválida")