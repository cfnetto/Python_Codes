# Faça um algoritmo que leia um conjunto de 20 números inteiros e indique, ao final, qual foi o menor valor digitado.

menor = float("inf")

for _ in range(20):
    numero = int(input("Digite um número inteiro: "))

    if numero < menor:
        menor = numero

print(f"O menor número digitado é {menor}")
