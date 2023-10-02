# Faça um programa que receba um valor que é o valor pago, um segundo valor que é o preço do produto e retorne o troco a ser dado

print("Qual o valor que foi pago?")
pago = float(input())
print("Qual o valor do produto?")
preco = float(input())

pago = pago - preco

if (pago >= 0):
    print("O troco é de " + str(pago))
else:
    print("O preco do produto é maior do que foi pago")
