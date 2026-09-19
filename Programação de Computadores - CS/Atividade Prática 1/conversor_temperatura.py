while True:
    try:
        graus_celsius = float(input("Digite uma temperatura em Celsius: ")) # A conversão é feita automaticamente durante a coleta da informação.
        graus_fahrenheit = (graus_celsius*9/5) + 32
        print(f"A temperatura\n{graus_celsius:g}° Celsius\ncorresponde à\n{graus_fahrenheit:g}° Fahrenheint")
        break
    except ValueError:
        print("Digite apenas números reais! E utilize (.) ao invés de (,).")