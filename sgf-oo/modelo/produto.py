class Produto:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.estoque = 0
    
    def __str__(self): # get nome
        return f'{self.nome} | {self.categoria} | {self.estoque}'