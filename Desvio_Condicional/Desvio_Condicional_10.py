# Faça um programa que solicita ao usuário três valores correspondentes aos lados de um triângulo. Informe se o triângulo é equilatero (possui três lados iguais), isóceles (possui dois lados iguais) ou escaleno (não possui lados iguais). Saídas:
# _Pedido para o usuário = "Digite três números inteiros: ";
# _Caso equilatero = "O triângulo é equilatero";
# _Caso isóceles = "O triângulo é isóceles";
# _Caso escaleno = "O triângulo é escaleno".

lado1 = float(input("Digite o tamanho do primeiro lado: "))
lado2 = float(input("Digite o tamanho do segundo lado: "))
lado3 = float(input("Digite o tamanho do terceiro lado: "))

if lado1 == lado2 and lado1 == lado3:
    print("O triângulo é equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é isóceles")
else:
    print("O triângulo é escaleno")
