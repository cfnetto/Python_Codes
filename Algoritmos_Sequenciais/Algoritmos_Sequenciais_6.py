# Faça um programa que solicita ao usuário dois números inteiros e armazena nas variáveis A e B.
# a) A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteudos fazendo com que o valor que está em A passe para B e vice-versa.
# b) Ao final escreva os valores que ficaram armazenados nas variáveis A e B respectivamente.

a = int(input("Digite um numero inteiro para ser armazenado na váriavel A: \n"))
b = int(input("Digite um numero inteiro para ser armazenado na váriavel B: \n"))

c = a
a = b
b = c

print("O número armazenado em A agora é " + str(a) +
      " e o número armazenado em B agora é " + str(b))
