# Faça um programa que solicita um número inteiro e exibe uma mensagem indicando se ele é positivo, negativo ou zero. Saídas:
# _Pedido ao usuário = "Digite um número inteiro: ";
# _Caso ele seja positivo = "Ele é positivo";
# _Caso ele seja negativo = "Ele é negativo";
# _Caso ele seja igual a zero = "Ele é igual a zero".

numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print("Ele é positivo")
elif numero < 0:
    print("Ele é negativo")
else:
    print("Ele é igual a zero")
