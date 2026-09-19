import random

secreto = random.randint(1, 101)
palpite = ""
tentativas = 0
limite = 10
print("=" * 21)
print("JOGO DAS ADIVINHAÇÕES")
print("=" * 21)
print(f"Um número secreto entre 1 e 100 foi escolhido! Tente adivinhá-lo dentro de {limite} tentativas para ganhar! Se quiser desistir basta digitar 0\n")

while tentativas < limite and palpite != secreto and palpite != 0: #Atenção
    try:
        palpite = int(input("Digite seu Palpite:"))
        if 0 <= palpite < 101:
            tentativas += 1
            if palpite == secreto:
                print(f"\nParabéns, você acertou o número secreto!\nSeu número de tentaivas foi: {tentativas}\n")
                break
            elif palpite == 0:
                print(f"Que pena! o número secreto era: {secreto}\n")
                break
            elif palpite > secreto:
                print("Muito Alto!")
                print(f"tentativas restantes: {limite-tentativas}\n")
            elif palpite < secreto:
                print("Muito Baixo!")
                print(f"tentativas restantes: {limite-tentativas}\n")
        else:
            print("Digite apenas números entre 1 e 100!")
            continue
    except ValueError:
        print("Digite apenas números inteiros, entre 1 e 100!")

if tentativas == limite:
    print(f"Você usou todas as tentativas, mas tudo bem você pode tentar novamente!\nO número secreto era: {secreto}")