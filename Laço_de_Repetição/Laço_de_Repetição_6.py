# Faça um programa que solicita ao usuário dois valores inteiros e positivos que serão a base e o expoente. O programa deve usar laço de repetição para calcular e escrever o resultado da base elevado ao expoente(potencia).

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

for _ in range(expoente):
    resultado *= base

print("O resultado da potência é " + str(resultado))
