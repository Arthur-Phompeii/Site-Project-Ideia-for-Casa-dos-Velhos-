registro_notas_alunos = [
    {"nome": "Arthur", "notas": [6.0, 2.4, 7.4, 10, 9.0]},
    {"nome": "Nota 10", "notas": [10, 10, 10, 10, 10]},
    {"nome": "Nota 5", "notas": [5, 5, 5, 5]},
    {"nome": "???", "notas": [5, 6.3, 8.9, 8.2, 5.1]},
    {"nome": "Teste com 0", "notas": [0, 0, 0, 0, 0]},
    {"nome": "Teste com nada", "notas": []},
]


def calcular_media(notas):
    """Função para calcular a média a partir de uma lista de notas

    Recebe:
        notas(list[float]): Lista de notas de determinado aluno.

    Retorna:
        float: resultado do cálculo da média"""
    soma = float()
    media = float()
    for nota in notas:
        soma += nota

    # medida de segurança contra possíveis listas vazias resultando em divisões por 0
    if len(notas):
        media = soma / len(notas)

    return round(media, 2)


def verificar_aprovacao(media, media_minima=7.0):
    """Função para verificar a aprovação de um aluno a partir de sua media

    Recebe:
        media(float): media de um aluno.
        media_minima(float): valor que determina a aprovação

    Retorna:
        string: resultado da aprovação"""

    if media < media_minima:
        return "Reprovado"
    elif media >= media_minima:
        return "Aprovado"


def gerar_relatorio(alunos):
    """Função para gerar um relatório da média e aprovação de todos os alunos

    Recebe:
        alunos(list[dict]): Lista de todos os alunos e suas respectivas notas

    Retorna:
        dict: Um relatório em dicionário com o resultado da aprovação de  todos os alunos registrados;
        str: Um Relatório em texto de todos os alunos registrados;"""

    relatorio_em_dicionario = {}
    relatorio_em_texto = ""
    # Proteção para caso a lista de alunos sejá informada em formato errado ou inexistente
    if isinstance(alunos, list) and all(isinstance(item, dict) for item in alunos):

        for cada_aluno in alunos:
            nome = cada_aluno["nome"]
            notas = cada_aluno["notas"]
            if len(notas) == 0:
                relatorio_em_texto += (
                    f"\nPor favor preencher as notas do aluno '{nome}'!\n"
                )
            media = calcular_media(notas)
            aprovacao = [media, verificar_aprovacao(media)]
            relatorio_em_dicionario[nome] = aprovacao

            relatorio_em_texto += f"O aluno '{nome}' obteve uma média de {aprovacao[0]} e por isso foi {aprovacao[1].upper()}\n"
    else:
        relatorio_em_texto += "Erro: Forneça uma lista de alunos e notas válida!"
        relatorio_em_dicionario.update(
            {"Erro": "Forneça uma lista de alunos e notas válida!"}
        )
    return relatorio_em_dicionario, relatorio_em_texto


if __name__ == "__main__":
    dicionario, texto = gerar_relatorio(registro_notas_alunos)
    print(texto)
