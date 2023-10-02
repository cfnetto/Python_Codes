# Faça um programa para uma calculadora simples que solicita ao usuário dois operandos como
# entrada, seleciona uma das opções da lista (1- soma, 2- produto, 3- divisão, 4- potência) e exibe
# o resultado. O algoritmo deve executar repetidamente até que os dois operandos informados
# sejam iguais a zero. Utilize uma variável do tipo real para exibir o resultado.

while True:
    operando1 = int(input("Digite o primeiro operando: "))
    operando2 = int(input("Digite o segundo operando: "))
    operador = int(input(
        "Digite qual das operações você deseja:\n1-Soma \n2-Produto \n3-Divisão \n4-Potência \n0-FIM\n"))

    if operador == 1:
        print("A soma dos dois operandos é igual a " + str(operando1 + operando2))
    elif operador == 2:
        print("O produto dos dois operandos é igual a " +
              str(operando1 * operando2))
    elif operador == 3:
        print("A divisão dos dois operadndos é igual a " +
              str(operando1 / operando2))
    elif operador == 4:
        print("A potência dos dois operandos é igual a " +
              str(operando1 ** operando2))
    elif operador == 0:
        break
    else:
        print("Nenhuma das opções diponiveis foi escolhida, tente novamente.")
