# Construa um algoritmo que solicite 5 valores inteiros ao usuário e os armazene em um vetor. Após, deverá ser invertido os valores do vetor utilizando um segundo vetor.

vetor = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

vetor_invertido = []

for i in range(len(vetor) - 1, -1, -1):
    vetor_invertido.append(vetor[i])

print("Vetor Invertido: ")

for i in range(len(vetor_invertido)):
    print(vetor_invertido[i], end="\t")
