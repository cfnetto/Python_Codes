# Faça um programa que solicita 20 valores inteiros e exiba quantos são pares e quantos são ímpares.

qtd_pares = 0
qtd_impares = 0

for _ in range(20):
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        qtd_pares += 1

    else:
        qtd_impares += 1

print(
    f"A quantidade de números pares é de {qtd_pares} e a quantidade de números ímpares é de {qtd_impares}")
