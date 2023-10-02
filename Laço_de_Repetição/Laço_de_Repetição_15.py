# Solicite ao usuário a digitação de um número inteiro, calcule e exiba o fatorial deste número

numero = int(input("Digite um número inteiro: "))
fatorial = 1

for i in range(1, numero+1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}")
