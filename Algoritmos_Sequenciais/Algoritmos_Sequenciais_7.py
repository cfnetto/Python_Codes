# Faça um programa que calcula os gastos com combustível em uma viagem.
# a) O programa deve solicitar ao usuário a distância a ser percorrida em Km, o consumo do carro em Km/litro e o preço do litro do combustível.
# b) Como resposta o programa deverá informar qual o valor em R$ a ser gasto com o combustível na viagem.

distancia = float(input("Qual a distância a ser percorrida na viagem?\n"))
consumo_carro = float(input("Qual o consumo do seu carro em Km/litro?\n"))
preco_gasolina = float(input("Qual o preço do combustível?\n"))

distancia /= consumo_carro

distancia *= preco_gasolina

print("Nesta viagem será gasto com combustível R$" + str(consumo_carro))
