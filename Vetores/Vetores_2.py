# Calcule a média das notas de 10 alunos de uma disciplina e determine o número de alunos que tiveram nota superior a média calculada.

notas = []

for _ in range(10):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)

media = sum(notas) / len(notas)

contador_medias = 0

for i in range(len(notas)):
    if notas[i] >= media:
        contador_medias += 1

print(
    f"O número de alunos que tiveram nota maior que a média {media} são {contador_medias} alunos")
