# Leia dois vetores A e B com vinte elementos. Construa um terceiro vetor C, onde cada elemento é a subtração do elemento correspondente de A com B.

vetor_A = []
vetor_B = []

for i in range(5):
    numero = int(
        input("Digite um número inteiro para ser alocado no vetor A: "))
    vetor_A.append(numero)

for i in range(20):
    numero = int(
        input("Digite um número inteiro para ser alocado no vetor B: "))
    vetor_B.append(numero)

vetor_C = []

for i in range(len(vetor_A)):
    vetor_C.append(vetor_A[i] - vetor_B[i])

print("Vetor C, feito com a subtração dos elementos dos vetores A e B: ")
for i in range(len(vetor_C)):
    print(vetor_C[i], end="\t")
