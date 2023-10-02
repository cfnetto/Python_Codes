# Faça um programa que solicita ao usário uma letra e verifique se ela é uma vogal ou não exibindo uma mensagem correspondente. Saídas
# _Pedido ao usuário = "Digite uma letra: ";
# _Caso verdadeiro = "É uma vogal";
# _Caso falso = "Não é uma vogal".

letra = str(input("Digite uma letra: "))


if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("É uma vogal")
else:
    print("Não é uma vogal")
