# Construa um algoritmo que solicite 5 valores ao usuário, armazene estes em um vetor de 5 posições inteiras. Após verifique se o número 7 se encontra no vetor. Em caso positivo, exiba qual a posição em que ele foi encontrado. Se ele for encontrado mais de uma vez também quantas vezes ele foi encontrado.

vetor = []
pos_sete = []
qtd_sete = 0

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

for i in range(len(vetor)):
    if vetor[i] == 7:
        pos_sete.append(i+1)
        qtd_sete += 1

print(f"\nO número 7 aparece {qtd_sete} vezes.")

if qtd_sete > 0:
    print("\nNas posições: ")
    for i in range(len(pos_sete)):
        print(pos_sete[i], end="\t")
