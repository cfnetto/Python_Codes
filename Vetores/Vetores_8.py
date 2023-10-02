# Leia 30 valores e jogue os pares em um vetor e os ímpares em outro. Após a leitura calcule o somatório dos dois vetores e exiba o de maior valor.

vetor_pares = []
vetor_impares = []

for i in range(30):
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        vetor_pares.append(numero)
    else:
        vetor_impares.append(numero)

soma_pares = sum(vetor_pares)
soma_impares = sum(vetor_impares)

if soma_impares > soma_pares:
    print("Vetor de Impares: ")
    for i in range(len(vetor_impares)):
        print(vetor_impares[i], end="\t")

elif soma_pares > soma_impares:
    print("Vetor de Pares: ")
    for i in range(len(vetor_pares)):
        print(vetor_pares[i], end="\t")
