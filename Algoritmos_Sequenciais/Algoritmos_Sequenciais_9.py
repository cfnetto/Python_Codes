# João recebeu seu salário S1 (em reais) e precisa pagar duas contas (C1 e C2) que estão atrasadas. Como as contas estão atrasadas, João terá de pagar  multa de 2% sobre cada conta. Faça um algoritmo que calcule e mostre quanto restará do salário do João.

S1 = float(input("Quanto João recebe de salário?\n"))
C1 = float(input("Qual o valor da primeira conta?\n"))
C2 = float(input("Qual o valor da segunda conta?\n"))

C1 *= 1.02
C2 *= 1.02

sobra_salario = S1 - (C1 + C2)

print("O que sobrará do salário de João é " + str(sobra_salario))
