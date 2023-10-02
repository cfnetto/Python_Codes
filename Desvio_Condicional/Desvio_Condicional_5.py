# Faça um programa que solicita ao usuário dois números inteiros. O primeiro é o valor das horas e o segundo dos minutos. Verifique se a hora é valida e exiba uma mensagem correspondente (considera a hora 24:00 como inválida). Saídas:
# _Pedido para horas = "Entre com um número para as horas: ";
# _Pedido para os minutos = "Entre com um número para os minutos: ";
# _Caso verdadeiro = "A hora é válida";
# _Caso falso = "A hora é inválida".

hora = int(input("Entre com um número para as horas: "))
minutos = int(input("Entre com um número para os minutos: "))

if hora >= 24 or minutos >= 60:
    print("A hora é inválida")
if hora < 24 and minutos < 60:
    print("A hora é válida")
