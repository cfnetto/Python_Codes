# Faça um programa que exiba na tela a tabuada do número 5 no seguinte formato: 5x1=5; 5x2=10; 5x3=15; ... 5x10=50.

for i in range(1, 11):
    print("5x" + str(i) + "=" + str(5*i))
