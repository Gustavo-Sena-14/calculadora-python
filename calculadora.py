def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

print("=== Calculadora em Python ===")
print("Operações disponíveis: soma, subtração, multiplicação, divisão")

op = input("Digite a operação desejada: ").strip().lower()
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

if op == "soma":
    print("Resultado:", soma(x, y))
elif op == "subtração" or op == "subtracao":
    print("Resultado:", subtracao(x, y))
elif op == "multiplicação" or op == "multiplicacao":
    print("Resultado:", multiplicacao(x, y))
elif op == "divisão" or op == "divisao":
    print("Resultado:", divisao(x, y))
else:
    print("Operação inválida!")
