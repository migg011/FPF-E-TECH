
def somar(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def calcular():
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    entrada = input("Qual operação? (soma/subtracao/multiplicacao/divisao): ").lower()

    if entrada == "soma":
        print(somar(numero1, numero2))
    elif entrada == "subtracao":
        print(subtracao(numero1, numero2))
    elif entrada == "multiplicacao":
        print(multiplicacao(numero1, numero2))
    elif entrada == "divisao":
        resultado = divisao(numero1, numero2)
        print(resultado)

    return input("Deseja sair? (SIM/NAO): ").lower()


# Programa principal
saida = "nao"
while saida == "nao":
    saida = calcular()