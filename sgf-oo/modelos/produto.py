class Produto:
    produtos = []
    def __init__(self, nome, categoria, preco_f, preco_v):
        self._nome = nome.title()
        self._categoria = categoria.upper
        self._estoque = 0
        self._preco_fabrica=preco_f
        self._preco_venda=preco_v
        self._precisa_de_receita=False
        Produto.produtos.append(self)
    
    def __str__(self): # get nome
        return f'{self.nome} | {self.categoria} | {self.estoque} | {self.preco_fabrica} | {self.preco_venda}'
    
    @classmethod
    def exibir_estoque(cls):
        print(f'{'Nome do Produto'.ljust(20)}|{'Categoria'.ljust(20)}|{'Custo'.ljust(20)}|{'Preço'.ljust(20)}Estoque')
        for produto in Produto.produtos:
            print(f'{produto.nome.ljust(20)}|{produto.categoria.ljust(20)}|{str(produto.preco_fabrica).ljust(20)}|{str(produto.preco_venda).ljust(20)}|{produto.estoque} unidades em estoque.')
        print()

    def registrar_entrada(self, qtde):
        self._estoque+=qtde
    