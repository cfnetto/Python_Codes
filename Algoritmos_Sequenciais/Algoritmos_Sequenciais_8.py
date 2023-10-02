# O sistema de avaliação de determinada disciplina, é composto por três provas. A primeira prova tem peso 2, a segunda tem peso 4  e a terceira tem peso 6. Faça um programa que solicita as notas, calcula e exibe a média final desse aluno.

nota1 = float(input("Digite a primeira nota com peso 2: "))
nota2 = float(input("Digite a segunda nota com peso 4: "))
nota3 = float(input("Digite a teceira nota com peso 6: "))

media_final = (nota1 * 2) + (nota2 * 4) + (nota3 * 6)
media_final /= 12

print("A média final deste aluno é: " + str(round(media_final, 2)))
