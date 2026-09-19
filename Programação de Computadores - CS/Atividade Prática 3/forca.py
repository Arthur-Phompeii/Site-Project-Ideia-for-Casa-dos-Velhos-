import random

# variáveis globais
sair = False
NUMERO_DE_TENTATIVAS_CONFIG = int(7)
numero_de_tentativas = NUMERO_DE_TENTATIVAS_CONFIG

# lista de palavras do jogo(diminuida na versão enviada ao professor)
palavras_do_jogo = {
    "BOLO": "É uma comida comemorativa",
    "CAMA": "Objeto de descanso",
    "SANTUARIO": "Lugar Sagrado",
    "ABACAXI": "Fruta tropical com casca espinhosa",
    "AVIAAO": "Meio de transporte aéreo",
    "BICICLETA": "Veículo de duas rodas movido a pedal",
    "CADEIRA": "Objeto usado para sentar",
    "CACHORRO": "Melhor amigo do homem",
    "COMPUTADOR": "Máquina usada para programação e estudos",
    "DINOSSAURO": "Animal pré-histórico extinto",
    "ELEFANTE": "Maior mamífero terrestre",
    "ESCOLA": "Lugar de aprendizado",
    "FOGUETE": "Veículo usado em viagens espaciais",
    "GELADEIRA": "Eletrodoméstico que mantém alimentos frios",
    "GIRAFA": "Animal de pescoço comprido",
    "HOSPITAL": "Lugar destinado a cuidados médicos",
    "JANELA": "Abertura em paredes para entrada de luz",
    "LANTERNA": "Objeto portátil de iluminação",
    "MACARRAO": "Massa muito consumida no almoço",
    "MONTANHA": "Grande elevação natural de terra",
    "NOTEBOOK": "Computador portátil",
    "OCEANO": "Grande massa de água salgada",
    "PIPOCA": "Comida típica de cinema",
    "QUEIJO": "Alimento derivado do leite",
    "RELAMPAGO": "Descarga elétrica atmosférica",
    "SORVETE": "Sobremesa gelada",
    "TELEVISAO": "Aparelho usado para assistir programas",
    "UNIVERSO": "Conjunto de tudo que existe",
    "VIOLAO": "Instrumento musical de cordas",
    "XADREZ": "Jogo de estratégia muito famoso",
    "ZEBRA": "Animal listrado preto e branco",
    "ALGORITMO": "Sequência lógica de instruções",
    "PYTHON": "Linguagem de programação famosa",
    "VARIAVEL": "Espaço usado para armazenar valores",
    "FUNÇAO": "Bloco reutilizável de código",
    "DICIONARIO": "Estrutura de dados com chave e valor",
    "LOOP": "Estrutura de repetição",
    "BOOLEANO": "Tipo lógico verdadeiro ou falso",
    "OBJETO": "Instância de uma classe",
    "CLASSE": "Molde para criar objetos",
    "HERANÇA": "Conceito de orientação a objetos",
}


def embaralhar_palavras(lista):
    """Embaralha o dicionário:

    Parâmetro:
        lista(dict):lista de palavras pré-definidas

    Retorna:
        dict: um novo dicionário embaralhado"""

    # transforma o dicionário em uma lista para que possa ser embaralhado
    embaralhador = list(lista.items())
    # embaralha a nova lista
    random.shuffle(embaralhador)
    # transforma a lista em um dicionáro novamente
    palavras_embaralhadas = dict(embaralhador)
    return palavras_embaralhadas


lista_palavras = embaralhar_palavras(palavras_do_jogo)


def preparar_partida(lista_partida):
    """Define todas as variáveis para uma nova partida

    Parâmetro:
        lista_partida(dict): lista de palavras embaralhadas

    Retorna:
        palavra_correta(list[str]): lista de caracteres da palavra escolhida
        dica(str): frase que contém a dica
        palavra_secreta(list[str]): versão com lacunas da palavra escolhida
        regsitro_de_palpites(set[str]): lista para armazenar os palpites sem duplicidade
        mostrar_dica(bool): define se a dica será mostrada"""

    # define a palavra da partida
    palavra_escolhida = lista_partida.popitem()

    # define a lista de letras da palavra e a dica
    palavra_correta = list(palavra_escolhida[0])
    dica = palavra_escolhida[1]

    # define a palavra com lacunas
    palavra_secreta = []
    for each_letra in palavra_correta:
        palavra_secreta.append("_")

    # zera a contagem de palpites
    # uso de set() para evitar duplicidade de registros
    registro_de_palpites = set()

    # zera contagem da dica
    mostrar_dica = False
    return palavra_correta, dica, palavra_secreta, registro_de_palpites, mostrar_dica


def processar_palpite(
    palpite, palavra, palavra_escondida, registro_palpites, registro_tentativas
):
    """Processa um palpite do jogador.

    Parâmetros:
        palpite (str): entrada do usuário.
        palavra (list[str]): palavra correta em lista.
        palavra_escondida (list[str]): estado atual com lacunas.
        registro_palpites (set[str]): letras já tentadas.
        registro_tentativas (int): tentativas restantes.

    Retorna:
        int: novo número de tentativas restantes."""

    if palpite in registro_palpites:
        print("\nVocê já deu esse palpite!")

    # verifica o palpite(caso seja uma letra)
    elif len(palpite) == 1:
        if palpite in palavra:
            for i, letra in enumerate(palavra):
                if letra == palpite:
                    palavra_escondida[i] = letra
        else:
            registro_tentativas -= 1
            print("\nErrou! Essa plavra não contém essa letra")
        registro_palpites.add(palpite)

    # verifica o palpite (caso seja uma palavra)
    elif len(palpite) == len(palavra):
        if palavra == list(palpite):
            print("\nAcertou! Essa é a palavra.")
            for i, letra in enumerate(palavra):
                palavra_escondida[i] = letra
        else:
            registro_tentativas -= 1
            print("\nErrou! Não é essa plavra")
    else:
        print(
            "Para dar um palpite, digite apenas uma letra. Você também pode chutar a palavra inteira, mas se errar, custará uma tentativa."
        )
    return registro_tentativas


# Mensagem de boas-vindas
print("=" * 70)
print(
    f"Bem vindo ao jogo da forca! \nVocê possui {numero_de_tentativas} tentivas e pode receber palavras fáceis ou dificeis!\nPara pedir uma dica basta digitar 'dica', ou digite 'sair' para encerrar o jogo."
)

# Define o loop de partidas do jogo
while lista_palavras:
    if sair == True:
        break
    elif numero_de_tentativas != 0:
        palavra, dica, palavra_escondida, registro_palpites, mostrar_dica = (
            preparar_partida(lista_palavras)
        )
    else:
        print("=" * 70)
        print("Acabaram as tentativas, foi quase!\n   A palavra era:", "".join(palavra))
        break
    """MENSAGEM AO ORIENTADOR: Não é possível declarar a variável antes da verificação, pois dessa forma um novo valor seria atribuído à variável 'palavra', e seria impresso a palavra errada no terminal. Também não faz sentido mantê-la em uma variável global, pois de qualquer forma, esse trecho de código só é reproduzido após a primeira chamada da função que declara a variável 'palavra'. A única coisa que pude alterar, foi inverter a ordem de chamada da função a partir da inversão da validação do número de tentativas para != 0, mas isso não resolve diretamente o problema, pois de qualquer forma a variável só é declarada após a validação da condição, o que eu particularmente considero pior, mas deixei a alteração para a sua orientação."""

    # Define o loop de palpites de uma partida
    while numero_de_tentativas != 0 and palavra != palavra_escondida:
        # informações principais
        print("=" * 70)
        print(f"> Tentivas restantes: {numero_de_tentativas}")
        if registro_palpites:
            print("> Palpites:", " ".join(sorted(registro_palpites)))
        print("Sua palavra é:")
        print(" ".join(palavra_escondida))
        if mostrar_dica == True:
            print(f"> A sua dica é: {dica}")
        palpite = input("Adivinhe uma letra: ").upper()

        # cadeia de if-elif para tomada de decisões
        if palpite == "DICA":
            mostrar_dica = True
        elif palpite == "SAIR":
            print("\nQue pena! A palavra era:", "".join(palavra))
            print("=" * 70)
            sair = True
            break
        else:
            numero_de_tentativas = processar_palpite(
                palpite,
                palavra,
                palavra_escondida,
                registro_palpites,
                numero_de_tentativas,
            )

            # verifica se a palavra foi totalmente adivinhada
            if palavra == palavra_escondida:
                print(" ".join(palavra_escondida))
                print("=" * 70)
                print(
                    "Parabéns, você acertou a palavra!\n\nUma nova palavra será escolhida, deseja continuar?"
                )
                continuar = input(
                    "Pressione Enter para continuar ou digite 'sair' para encerrar o jogo: "
                ).upper()
                if continuar == "SAIR":
                    sair = True
                    print("=" * 70)
                    break
                else:
                    numero_de_tentativas = NUMERO_DE_TENTATIVAS_CONFIG
                    continue
if len(lista_palavras) == 0:
    print("Você encerrou todas as palavras, parabéns!")

# python forca.py

# quando está na ultima palavra (ou seja, lista de palavras está vazia) a mensagem de parabens aparece do mesmo jeito
