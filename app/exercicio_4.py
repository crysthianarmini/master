
class Usuario:
    def __init__(self,nome,cep) -> None:
        self.nome = nome
        self.valor = cep

class Product:

    def __init__(self,nome,valor) -> None:
        self.nome = nome
        self.valor = valor


class Cart:

    def __init__(self,usuario) -> None:
        self.usuario = usuario
    
    lista_produtos = []
    
    def valor_total_carrinho(self,lista_produtos):
        valor_total = 0
        for item in lista_produtos:
            valor_total += item.valor
        return valor_total
    

