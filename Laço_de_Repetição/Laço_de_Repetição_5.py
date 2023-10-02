# Faça um programa que exiba na tela a soma dos números inteiros do intervalo [100, 200].
# Exemplo: soma = 100 + 101 + 102 + ... + 200.

soma = 0

for i in range(100, 201, 1):
    soma += i
    print(soma)
