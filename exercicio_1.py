'''
Exercício 1 - Múltiplos de 3 ou 5

Dado todos os números naturais abaixo de 10;
Se selecionarmos aqueles que sejam múltiplos de 3 ou 5 temos: 3, 5, 6 e 9.
Se somarmos todos esses valores, teremos o resultado = 23
Desenvolva um sistema que responda às seguintes dúvidas:
Qual é o valor da soma de todos os números múltiplos de 3 ou 5 de números naturais abaixo de 1000?
Qual é o valor da soma de todos os números múltiplos de 3 e 5 de números naturais abaixo de 1000?
Qual é o valor da soma de todos os números múltiplos de (3 ou 5) e 7 de números naturais abaixo de 1000?
'''
import unittest

# Exercício
def multiplo_tres_ou_cinco(valor_base):
    valor_inicial = 0

    for numero_atual in range(valor_base):
        if numero_atual % 3 == 0 or numero_atual % 5 == 0:
            valor_inicial += numero_atual

    return valor_inicial


def multiplo_tres_e_cinco(valor_base):
    valor_inicial = 0

    for numero_atual in range(valor_base):
        if numero_atual % 3 == 0 and numero_atual % 5 == 0:
            valor_inicial += numero_atual

    return valor_inicial

def multiplo_tres_ou_cinco_e_sete(valor_base):
    valor_inicial = 0

    for numero_atual in range(valor_base):
        if (numero_atual % 3 == 0 or numero_atual % 5 == 0) and numero_atual%7==0:
            valor_inicial += numero_atual

    return valor_inicial


# Testes
class Test(unittest.TestCase):
    def testando_multiplos_de_3_e_5_abaixo_de_mil(self):
        actual = multiplo_tres_e_cinco(1000)
        expected = 33165
        self.assertEqual(actual, expected)

    def testando_multiplos_de_3_ou_5_abaixo_de_mil(self):
        actual = multiplo_tres_ou_cinco(1000)
        expected = 233168
        self.assertEqual(actual, expected)
    
    def testando_multiplos_de_3_ou_5_e_sete_abaixo_de_mil(self):
        actual = multiplo_tres_ou_cinco_e_sete(1000)
        expected = 33173
        self.assertEqual(actual, expected)