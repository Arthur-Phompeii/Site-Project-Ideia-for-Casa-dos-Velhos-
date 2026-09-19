import unittest

# =========================
# CÓDIGO A SER TESTADO

from gerenciador_notas import registro_notas_alunos, calcular_media, verificar_aprovacao, gerar_relatorio

# =========================
# TESTES

class TestesSistemaNotas(unittest.TestCase):

    # -------------------------
    # TESTES calcular_media
    # -------------------------

    def test_media_arthur(self):

        resultado = calcular_media(
            registro_notas_alunos[0]["notas"]
        )

        self.assertEqual(resultado, 6.96)


    def test_media_nota_10(self):

        resultado = calcular_media(
            registro_notas_alunos[1]["notas"]
        )

        self.assertEqual(resultado, 10.0)


    def test_media_nota_5(self):

        resultado = calcular_media(
            registro_notas_alunos[2]["notas"]
        )

        self.assertEqual(resultado, 5.0)

    def test_media_nome_caractere(self):

        resultado = calcular_media(
            registro_notas_alunos[3]["notas"]
        )

        self.assertEqual(resultado, 6.7)

    def test_media_com_zero(self):

        resultado = calcular_media(
            registro_notas_alunos[4]["notas"]
        )

        self.assertEqual(resultado, 0)

    def test_media_lista_vazia(self):

        resultado = calcular_media(
            registro_notas_alunos[5]["notas"]
        )

        self.assertEqual(resultado, 0.0)

    # -------------------------
    # TESTES verificar_aprovacao
    # -------------------------

    def test_aprovado(self):

        resultado = verificar_aprovacao(8.5)

        self.assertEqual(resultado, "Aprovado")


    def test_reprovado(self):

        resultado = verificar_aprovacao(4.0)

        self.assertEqual(resultado, "Reprovado")


    def test_aprovado_no_limite(self):

        resultado = verificar_aprovacao(7.0)

        self.assertEqual(resultado, "Aprovado")

    def test_nota_corte_zero(self):

        resultado = verificar_aprovacao(0.0, media_minima=0.0)

        self.assertEqual(resultado, "Aprovado")

    # -------------------------
    # TESTES gerar_relatorio
    # -------------------------

    def test_relatorio_retorna_dicionario(self):

        relatorio, texto = gerar_relatorio(
            registro_notas_alunos
        )

        self.assertIsInstance(relatorio, dict)


    def test_relatorio_retorna_texto(self):

        relatorio, texto = gerar_relatorio(
            registro_notas_alunos
        )

        self.assertIsInstance(texto, str)


    def test_relatorio_contem_arthur(self):

        relatorio, texto = gerar_relatorio(
            registro_notas_alunos
        )

        self.assertIn("Arthur", relatorio)


    def test_relatorio_media_arthur(self):

        relatorio, texto = gerar_relatorio(
            registro_notas_alunos
        )

        self.assertEqual(
            relatorio["Arthur"][0],
            6.96
        )


    def test_relatorio_aprovacao_arthur(self):

        relatorio, texto = gerar_relatorio(
            registro_notas_alunos
        )

        self.assertEqual(
            relatorio["Arthur"][1],
            "Reprovado"
        )

    def test_relatorio_texto(self):

        relatorio, texto = gerar_relatorio(
            registro_notas_alunos
        )

        self.assertIn(
            "O aluno 'Arthur'",
            texto
        )

    def test_relatorio_tipo_invalido(self):

        relatorio, texto = gerar_relatorio(
            ["isso", "não", "é", "dict"]
        )

        self.assertIn(
            "Erro:",
            texto
        )


# =========================
# EXECUÇÃO DOS TESTES

if __name__ == "__main__":
    unittest.main()