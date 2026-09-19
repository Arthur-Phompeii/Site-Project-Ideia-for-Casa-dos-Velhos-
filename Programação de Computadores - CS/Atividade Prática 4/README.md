Esse sistema realiza o cálculo da média a partir de uma lista de alunos com suas respectivas notas, e gera um relatório informando sua aprovação.

Para executar o código principal basta declarar a função 'gerar_relatorio(registro_notas_alunos)' passando a devida variável como argumento.
A função 'gerar_relatorio()' retorna dois valores de interesse, sendo eles:
    relatorio_em_dicionario: O qual fornece as informações necessárias em formato de diconário;

    relatorio_em_texto: O qual fornce as informações de forma mais legível, em uma String.
Basta escolher a forma de saída desejada.
    

É válido lembrar que a variável 'registro_notas_alunos' é uma lista de dicionários e deve estar preenchida com as informações no seguinte formato:
    {
        "nome": "nome do aluno",
        "notas": [
        nota 1, nota 2, nota 3, nota 4 ...
    ]},
Atente-se para não deixar a lista de notas de um aluno vazia.

O arquivo test_notas.py foi usado como ambiente de testes, para iniciá-lo basta executar:
    if __name__ == "__main__":
        unittest.main()