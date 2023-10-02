# Declare um vetor de 10 inteiros, leia um valor para cada posição e no final mostre a média, o menor e o maior valor contidos no vetor

vetor = []
menor = 0
maior = 0
media = 0

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

media = sum(vetor) / len(vetor)
maior = max(vetor)
menor = min(vetor)

print(
    f"A média dos valores digitados é {media}, o maior valor digitado é {maior} e o menor valor digitado é {menor}")
