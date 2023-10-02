# Faça um programa que solicita ao usuário um valor inteiro e exibe uma mensagem informando se o número é par ou ímpar. Saídas:
# _Pedido ao usuário = "Entre com um número inteiro: ";
# _Caso verdadeiro = "O número é par";
# _Caso falso = "O númeor é ímpar".

numero = int(input("Entre com um número inteiro: "))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
