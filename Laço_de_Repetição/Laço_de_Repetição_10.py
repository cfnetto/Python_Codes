# Faça um programa que solicita ao usuário o valor de N e calcule o valor de S na série S = 1/1 + 1/2 + 1/3 + ... + 1/N. Ao fim exiba o número real resultante da série.

s = 0
n = int(input("Digite o valor de N: "))

for i in range(1, n+1):
    s += 1/i

print("O valor final de S é igual a " + str(round(s, 2)))
