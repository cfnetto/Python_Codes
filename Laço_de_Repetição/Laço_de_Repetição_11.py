# Faça um programa que solicita a idade de 10 pessoas e exiba a quantidade de pessoas que possui idade maior ou igual a 18 anos

pessoas_maiores = 0

for i in range(10):
    idade = int(input("Digite a idade da pessoa: "))

    if idade >= 18:
        pessoas_maiores += 1

print("A quantidade de pessoas maiores de idade é de " + str(pessoas_maiores))
