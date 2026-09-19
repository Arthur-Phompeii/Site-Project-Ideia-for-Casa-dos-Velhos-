import math

while True:
    try:
        fatorial = int(input("Cálculo de Fatorial (Escolha um número de 1 a 10):")) # A conversão é feita diretamente na coleta de dados pelo input
        resultado_fatorial = math.factorial(fatorial)
        print(f"O resultado do fatorial de {fatorial}! é {resultado_fatorial}.")
    except ValueError:
        print("Digite apenas números inteiros!")