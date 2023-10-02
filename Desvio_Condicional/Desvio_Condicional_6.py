# Faça um programa que exiba o maior dentre dois números reais digitados pelo usuário. Caso eles sejam iguais exiba uma mensagem correspondente. Saídas:
# _Pedido ao usuário = "Digite dois números reais: ";
# _Caso eles sejam iguais = "Eles são iguais".
# _Caso eles sejam diferentes exiba somente o número desejado.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 == numero2:
    print("Eles são iguais")
elif numero1 > numero2:
    print("O maior número é " + str(numero1))
else:
    print("O maior número é " + str(numero2))
