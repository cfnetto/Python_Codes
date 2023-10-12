# Faça o programa principal que solicita ao usuário um número inteiro N e após faça a chamada de um procedimento com o nome de "castigo", passando N como parâmetro por valor. O valor procedimento deve imprimir N vezes a frase "Não vou colar na prova".

def castigo(N):
    for _ in range(N):
        print("Não vou colar na prova")


N = int(input("Digite um número inteiro: "))
castigo(N)
