# Faça um programa que solicita ao usuário seu nome e as notas de notas de três provas. Calcule a média aritimética e informe se o aluno foi Aprovado ou Reprovado (o aluno é considerado aprovado com a média igual a superio a 6). Saídas:
# _Pedido ao usuário = "Digite as notas a seguir:";
# _Caso nota maior que 6 = "Você foi aprovado";
# _Caso nota menor que 6 = "Você foi reprovado".

nota1 = float(input("Digite a nota a seguir: "))
nota2 = float(input("Digite a nota a seguir: "))
nota3 = float(input("Digite a nota a seguir: "))

media = nota1 + nota2 + nota3
media /= 3

if media >= 6:
    print("Você foi aprovado")
elif media < 6:
    print("Você foi reprovado")
