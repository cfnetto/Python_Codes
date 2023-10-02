# Declare um vetor de 10 inteiros, leia um valor para cada posição e no final mostre o calculo do fatorial do maior e do menor.

vetor = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

maior = vetor[0]
menor = vetor[0]

for i in range(1, 10, 1):
    if vetor[i] > maior:
        maior = vetor[i]

    if vetor[i] < menor:
        menor = vetor[i]

fatorial_maior = 1
fatorial_menor = 1

for i in range(maior, 1, -1):
    fatorial_maior *= i

for i in range(menor, 1, -1):
    fatorial_menor *= i

print(
    f"O fatorial do maior elemento ({maior}) é {fatorial_maior}, e o faatorial do menor elemento ({menor} é {fatorial_menor})")
