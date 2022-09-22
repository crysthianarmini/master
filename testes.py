import unittest
from app.exercicio_1 import Multiplos
from app.exercicio_2 import NumerosFeliz
from app.exercicio_3 import PalavrasEmNumeros
from app.exercicio_4 import Usuario, Product, Cart


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

    def testando_valor_negativo_multiplos(self):
        actual = Multiplos.multiplo_tres_e_cinco(-10)
        self.assertEqual(actual, 0)

        actual = Multiplos.multiplo_tres_ou_cinco(-10)
        self.assertEqual(actual, 0)

        actual = Multiplos.multiplo_tres_ou_cinco_e_sete(-10)
        self.assertEqual(actual, 0)


class TestesExercicio2(unittest.TestCase):

    def testando_soma_quadrados_digitos_verdadeiro(self):
        resultado_verdadeiro = NumerosFeliz.soma_quadrados_digitos(self, 22)
        teste_verdadeiro = 8
        self.assertEqual(resultado_verdadeiro, teste_verdadeiro)

    def testando_soma_quadrados_digitos_falso(self):
        resultado_verdadeiro = NumerosFeliz.soma_quadrados_digitos(self, -22)
        teste_falso = 0
        self.assertEqual(resultado_verdadeiro, teste_falso)

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
        resultado_teste = PalavrasEmNumeros.valor_resultante_caracteres(
            'abacate')
        resultado_esperado = 33
        self.assertEqual(resultado_teste, resultado_esperado)

    def testando_retorno_numerico_quando_tem_numero_na_palavra(self):
        resultado_teste = PalavrasEmNumeros.valor_resultante_caracteres(
            'abacate97')
        resultado_esperado = 33
        self.assertEqual(resultado_teste, resultado_esperado)

    def testando_se_retorna_um_numero_primo(self):
        resultado_teste = PalavrasEmNumeros.verifica_numero_primo(11)
        self.assertEqual(resultado_teste, True)

    def testando_se_nao_retorna_numero_primo(self):
        resultado_teste_false = PalavrasEmNumeros.verifica_numero_primo(15)
        self.assertEqual(resultado_teste_false, False)

    def testando_se_nao_retorna_numero_primo_quando_valor_negativo(self):
        resultado_teste_negativo = PalavrasEmNumeros.verifica_numero_primo(-11)
        self.assertEqual(resultado_teste_negativo, False)

    def testando_numero_feliz(self):
        resultado_teste = PalavrasEmNumeros.numero_feliz(7)
        self.assertEqual(resultado_teste, True)

    def testando_numero_multiplo_de_tres_ou_cinco(self):
        resultado_teste = PalavrasEmNumeros.verifica_multiplos(15)
        self.assertEqual(resultado_teste, True)

    def testanto_caracteristicas_do_numero(self):
        numero_primo = PalavrasEmNumeros.verifica_caracteristicas_numero(5)
        self.assertEqual(
            numero_primo, '- Numero é primo - Numero é multiplo de 3 ou 5 ')


class TestesExercicio4(unittest.TestCase):

    teste_usuario = Usuario('Joao', '29185000')
    teste_produto = Product('Celular', 1500)
    teste_carrinho = Cart(teste_usuario)

    def testando_classe_usuario(self, Usuario=teste_usuario):
        self.assertEqual(Usuario.nome, 'Joao')
        self.assertEqual(Usuario.cep, '29185000')

    def testando_classe_produto(self, Produto=teste_produto):
        self.assertEqual(Produto.nome, 'Celular')
        self.assertEqual(Produto.valor, 1500)

    def testando_classe_carrinho(self, Cart=teste_carrinho):
        self.assertEqual(Cart.usuario.nome, 'Joao')

    def testando_retorno_valor_total_compras(self,carrinho = teste_carrinho):
        carrinho.lista_produtos.append(Product('Celular',1500))
        carrinho.lista_produtos.append(Product('Monitor',1000))
        valor_total_carrinho = carrinho.valor_total_carrinho()
        self.assertEqual(valor_total_carrinho, 2500)
    
    def testando_carrinho_vazio(self, carrinho = teste_carrinho):
        valor_total_carrinho = carrinho.valor_total_carrinho()
        self.assertEqual(valor_total_carrinho, 0)
  

if __name__ == '__main__':
    unittest.main()
