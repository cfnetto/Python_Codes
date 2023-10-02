# Leia um valor do produto e adicione mais 15% de imposto. Escreva o preço final do produto.

preco = float(input("Digite o valor do produto: "))

preco += preco * 0.15

print("O preço do produto com 15% de imposto é igual a: " + str(preco))
