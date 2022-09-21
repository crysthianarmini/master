import unittest
from app.exercicio_1 import Multiplos
from app.exercicio_2 import NumerosFeliz
from app.exercicio_3 import PalavrasEmNumeros


class TestesExercicio1(unittest.TestCase):
    def testando_multiplos_de_3_e_5_abaixo_de_mil(self):
        actual = Multiplos.multiplo_tres_e_cinco(1000)
        expected = 33165
        self.assertEqual(actual, expected)

    def testando_multiplos_de_3_ou_5_abaixo_de_mil(self):
        actual = Multiplos.multiplo_tres_ou_cinco(1000)
        expected = 233168
        self.assertEqual(actual, expected)

    def testando_multiplos_de_3_ou_5_e_sete_abaixo_de_mil(self):
        actual = Multiplos.multiplo_tres_ou_cinco_e_sete(1000)
        expected = 33173
        self.assertEqual(actual, expected)


class TestesExercicio2(unittest.TestCase):

    def testando_numero_inteiro_positivo(self):
        resultado_verdadeiro = NumerosFeliz.numero_inteiro_positivo(self, 1)
        self.assertEqual(resultado_verdadeiro, True)

        resultado_falso = NumerosFeliz.numero_inteiro_positivo(self, -1)
        self.assertEqual(resultado_falso, False)

    def testando_soma_quadrados_digitos(self):
        resultado_verdadeiro = NumerosFeliz.soma_quadrados_digitos(self, 22)
        teste_verdadeiro = 8
        self.assertEqual(resultado_verdadeiro, teste_verdadeiro)

    def testando_numero_feliz_falso(self):
        verifica_numero_feliz = NumerosFeliz.numero_feliz(self, 22)
        self.assertEqual(verifica_numero_feliz, False)

    def testando_numero_feliz_verdadeiro(self):
        verifica_numero_feliz = NumerosFeliz.numero_feliz(self, 7)
        self.assertEqual(verifica_numero_feliz, True)


class TestesExercicio3(unittest.TestCase):

    def testando_desconsiderar_caracteres(self):
        resultado_teste = PalavrasEmNumeros.desconsiderar_caracteres(
            'Joao154Jose$%')
        resultado_esperado = 'JoaoJose'
        self.assertEqual(resultado_teste, resultado_esperado)

    def testando_palavra_em_valor_numerico(self):
        resultado_teste = PalavrasEmNumeros.valor_resultante_caracteres('a')
        resultado_esperado = 1
        self.assertEqual(resultado_teste, resultado_esperado)

    def testando_se_retorna_um_numero_primo(self):
        resultado_teste = PalavrasEmNumeros.verifica_numero_primo(11)
        self.assertEqual(resultado_teste, True)

    def testando_se_nao_retorna_numero_primo(self):
        resultado_teste_false = PalavrasEmNumeros.verifica_numero_primo(15)
        self.assertEqual(resultado_teste_false, False)

        resultado_teste_negativo = PalavrasEmNumeros.verifica_numero_primo(-11)
        self.assertEqual(resultado_teste_negativo, False)

    def testando_numero_feliz(self):
        resultado_teste = PalavrasEmNumeros.numero_feliz(7)
        self.assertEqual(resultado_teste, True)

    def testando_numero_multiplido_de_tres_ou_cinco(self):
        resultado_teste = PalavrasEmNumeros.verifica_multiplos(15)
        self.assertEqual(resultado_teste, True)


class TestesExercicio4(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
