# Faça uma função que recebe três números reais por parametro e retorne o maior deles.

def maior(numero1, numero2, numero3):
    return max(numero1, numero2, numero3)


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
maior_numero = maior(numero1, numero2, numero3)

print(f"O maior número entre os digitados é o {maior_numero}")
