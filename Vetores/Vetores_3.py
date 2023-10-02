# Declare um vetor de 5 inteiros, leia um valor para cada posição e no final mostre quantos elementos possuem valor maior, menor e igual ao primeiro elemento do vetor.

vetor = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

maior = 0
menor = 0
igual = 0

for i in range(len(vetor)):
    if vetor[i] > vetor[0]:
        maior += 1

    if vetor[i] < vetor[0]:
        menor += 1

    if vetor[i] == vetor[0]:
        igual += 1

print(
    f"A quantidade de elementos maiores que o primeiro elemento é {maior}, a quantidade de elementos menores que o primeiro elemento é igual a {menor} e a quantidade de elementos iguais ao primeiro elemento é igual a {igual - 1}")
