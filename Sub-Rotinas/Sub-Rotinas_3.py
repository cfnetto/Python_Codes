# Faça uma função que recebe, por parâmetro, a altura e o sexo de uma pessoa e retorna o seu peso ideal. Para os homens, calcular o peso ideal usando a fórmula PI = 72,7 * altura - 58, e para mulheres PI = 62,1 * altura - 44,7.

def imc(sexo, altura):
    if sexo == "masculino":
        pi = 72.7 * altura - 58
    elif sexo == "feminino":
        pi = 62.1 * altura - 44.7

    return pi


sexo = str(input("O IMC é do sexo masculino ou feminino?\n"))
altura = float(input("Digite a altura da pessoa: "))

peso_ideal = imc(sexo, altura)

print(f"O peso ideal dessa pessoa é {peso_ideal}")
