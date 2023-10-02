# Faça um programa que receba o valor do quilo do produto e a quantidade de quilos do produto consumida calculando o valor final a ser pago

preco_por_quilo = float(input("Qual o preço por quilo do produto?\n"))
qtd_quilos = float(input("Quantidade de quilos do produto comprado: \n"))

valor_final = preco_por_quilo * qtd_quilos

print("O valor final a ser pago é de R$" + str(valor_final))
