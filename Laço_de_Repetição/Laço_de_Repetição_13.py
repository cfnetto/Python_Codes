# Faça um programa que solicita o peso de 25 pessoas e exibe qual o maior peso e qual o menor peso entre os digitados.

maior_peso = 0
menor_peso = float("inf")

for _ in range(25):
    peso = float(input("Digite o peso da pessoa: "))

    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso:
        menor_peso = peso

print(f"O maior peso é {maior_peso} e o menor peso é {menor_peso}")
