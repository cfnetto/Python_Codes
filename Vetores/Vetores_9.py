# Faça um programa que leia dois vetores A e B, de tamanho 8, e realiza a troca dos elementos destes vetores; ou seja, após a execução do programa o vetor B deverá conter os valores fornecidos para o vetor A e vice-versa.

vetor_A = []
vetor_B = []

print("Vetor A: ")
for i in range(8):
    numero = int(input("Digite um número: "))
    vetor_A.append(numero)

print("Vetor B: ")
for i in range(8):
    numero = int(input("Digite um número: "))
    vetor_B.append(numero)

vetor_aux = []

for i in range(len(vetor_A)):
    vetor_aux.append(vetor_A[i])

for i in range(len(vetor_A)):
    vetor_A[i] = vetor_B[i]

print("\n\nVetores Invertidos: ")
print("\nVetor A: ")

for i in range(len(vetor_A)):
    print(vetor_A[i], end="\t")

print("\nVetor B: ")

for i in range(len(vetor_aux)):
    print(vetor_aux[i], end="\t")
