'''
Neste problema, dado uma palavra composta somente por letras [a-zA-Z], cada letra possui um valor específico,
 ‘a’ vale 1, ‘b’ vale 2 e assim por diante, até a letra ‘z’ que vale 26. Do mesmo modo ‘A’ vale 27, ‘B’ vale 28, até 
 a letra ‘Z’ que vale 52.
O valor da palavra será a soma total dos valores de todas as letras da palavra.
Você precisa definir se cada palavra em um conjunto de palavras é:
Prima ou não;
Feliz ou não;
Múltipla de 3 ou 5;
Qualquer caractere na palavra que não seja uma letra deve ser desconsiderado.

Definition of Done
Um sistema que, quando executado, transforme uma palavra em um número, seguindo a lógica acima, e responda às três 
questões: se é prima, feliz e múltipla de 3 ou 5.
Não há a necessidade de ter interação com o usuário para requisitar a palavra.
É esperado que as soluções anteriores sejam re-usadas, e cada novo componente criado seja coberto com testes 
automatizados.

'''
import re
import app.helpers as helpers
import app.exercicio_2 as exercicio2


class PalavrasEmNumeros:

    def desconsiderar_caracteres(palavra: str) -> str:
        palavra = re.sub('[0-9]', '', palavra)
        palavra = ''.join(char for char in palavra if char.isalnum())

        return palavra

    def valor_resultante_caracteres(palavra: str) -> int:
        soma_caracteres = 0
        palavra = PalavrasEmNumeros.desconsiderar_caracteres(palavra)
        for letra in palavra:
            valor_numerico = helpers.valores_alfabeto[letra]
            soma_caracteres += valor_numerico

        return soma_caracteres

    def verifica_numero_primo(valor: int) -> bool:
        if valor < 0:
            return False
        if valor == 0 or valor == 1:
            return False
        else:
            if valor == 2:
                return True
            elif valor % 2 == 0:
                return False
            else:
                x = 3
                while (x < valor):
                    if valor % x == 0:
                        break
                    x = x + 2
                if x == valor:
                    return True
                else:
                    return False

    def numero_feliz(valor: int) -> bool:
        verificar = exercicio2.NumerosFeliz()
        return verificar.numero_feliz(valor)

    def verifica_multiplos(valor: int) -> bool:
        if valor % 3 == 0 or valor % 5 == 0:
            return True
        else:
            return False
    
    def verifica_caracteristicas_numero(numero:int) -> str:
        response = ''
        if(PalavrasEmNumeros.verifica_numero_primo(numero) is True):
            response += '- Numero é primo '

        if(PalavrasEmNumeros.verifica_multiplos(numero)is True):
            response += '- Numero é multiplo de 3 ou 5 '

        if(PalavrasEmNumeros.numero_feliz(numero)is True):
            response += '- Numero é feliz '

        return response




