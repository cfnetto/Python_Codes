# Faça um programa que solicita ao usuário um número real positivo. Verifique se o número é
# realmente positivo, e em caso contrário solicite ao usuário digitar novamente (este processo
# pode se repetir inúmeras vezes e é chamado de consistência, pois garante que o número será
# válido após a entrada de dados). Saídas:
# _Pedido ao usuário = “Digite um número real positivo”;
# _Caso número valido = “O número digitado é valido”;
# _Caso número invalido = “Número invalido, tente novamente”.

while True:
    numero = float(input("Digite um número real positivo: "))
    if numero < 0:
        print("Número invalido, tente novamente")
    elif numero >= 0:
        print("O número digitado é valido")
        break
