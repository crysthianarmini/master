
class Usuario:
    def __init__(self,nome:str,cep:str) -> None:
        self.nome = nome
        self.cep = cep

class Product:

    def __init__(self,nome:str,valor:float) -> None:
        self.nome = nome
        self.valor = valor


class Cart:

    def __init__(self,usuario) -> None:
        self.usuario = usuario
    
    lista_produtos = []
    
    def valor_total_carrinho(self,lista_produtos=lista_produtos):
        valor_total = 0
        for item in lista_produtos:
            valor_total += item.valor
        return valor_total

class Correio:
    
    def __init__(self,cep:str) -> float:
        self.cep = cep
        return 10.5


