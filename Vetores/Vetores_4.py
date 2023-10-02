# Declare um vetor de 10 inteiros, leia um valor para cada posição e no final mostre os elementos deste vetor em posição inversa ao que foram atribuídos

vetor = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

print("Vetor com as posições invertidas: ")

for i in range(9, -1, -1):
    print(vetor[i])
