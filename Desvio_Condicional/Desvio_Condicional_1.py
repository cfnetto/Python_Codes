# Faça um programa que solicita ao usuário um número inteiro e exibe este na tela. Se o número for negativo, antes de ser exibido, ele deve ser transformado no equivalente positivo.

numero = int(input("Digite um número inteiro: "))

if numero < 0:
    numero *= -1
    print("O número digitado transformado em positivo é " + str(numero))
else:
    print("O número digitado é " + str(numero))
