# Faça um programa que solicita a data de nascimento de uma pessoa e a data atual e exibe a idade desta pessoa em anos. (A data deve ser armazenada em 3 variáveis inteiras para ano, mês e dia).

dia_nascimento = int(input("Digite o dia de nascimento da pessoa: "))
mes_nascimento = int(input("Digite o mês de nascimento da pessoa: "))
ano_nascimento = int(input("Digite o ano de nascimento da pessoa: "))
dia_atual = int(input("Digite o dia atual: "))
mes_atual = int(input("Digite o mês atual: "))
ano_atual = int(input("Digite o ano atual: "))

if mes_atual > mes_nascimento:
    idade = ano_atual - ano_nascimento
if mes_atual < mes_nascimento and dia_atual < dia_nascimento:
    idade = (ano_atual - ano_nascimento) - 1
if mes_atual == mes_nascimento and dia_atual < dia_nascimento:
    idade = (ano_atual - ano_nascimento) - 1
if mes_atual == mes_nascimento and dia_atual >= dia_nascimento:
    idade = ano_atual - ano_nascimento

print("A idade da pessoa é " + str(idade))
