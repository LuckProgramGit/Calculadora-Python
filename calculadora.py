def somar (num1, num2):
    total = num1 + num2
    return total
def divide (num1, num2):
    total = num1 / num2
    return total

def subtrai (num1, num2):
    total = num1 - num2
    return total

def mutiplica (num1, num2):
    total = num1 * num2
    return total

def potencia (num1, num2):
    total = num1 ** num2
    return total

num1 = float(input("Digite o primeiro número: ")) 
num2 = float(input("Digite o segundo número: "))

print("""
Escolha uma operação:
1 - Soma:
2 - Dividir:
3 - Subtrair:
4 - Mutiplicar:
5 - Potencia:
""")


operacao = int(input("Operacao: "))

if operacao == 2 and num2 == 0:
    print("Não é possivel dividir por zero")
else:
    if operacao == 1:
        print("Resultado", somar(num1, num2))
    elif operacao == 2:
        print("Resultado", divide(num1, num2))
    elif operacao == 3:
        print("Resultado", subtrai(num1, num2))
    elif operacao == 4:
        print("Resultado", mutiplica(num1, num2))
    elif operacao == 5:
        print("Resultado", potencia(num1, num2))
    else:
        print("Operação inválida!")