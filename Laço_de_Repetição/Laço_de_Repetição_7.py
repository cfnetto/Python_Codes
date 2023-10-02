# Faça um programa que solicita ao usuário uma quantidade indeterminada de números inteiros. O programa deve calcular e escrever a média aritmética apenas dos números pares. A entrada de dados deve ser encerrada quando o número 0 (ZERO) for digitado.

soma = 0
media = 0
cont = 0

while True:
    numero = int(input("Digite um número inteiro: "))

    if numero == 0:
        break
    elif numero % 2 == 0:
        soma += numero
        cont += 1

if cont > 0:
    media = soma / cont
    print("A média dos números pares digitados é igual a " + str(media))
else:
    print("Nenhum número par foi digitado")
