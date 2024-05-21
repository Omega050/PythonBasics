
class Produto:
    produtos = []

    def __init__(self, nome, categoria, preco_f, preco_v):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._estoque = 0
        self._preco_fabrica=preco_f
        self._preco_venda=preco_v
        Produto.produtos.append(self)

    def __str__(self):  # get nome
        return f'{self.nome}|{self.categoria}|{self.estoque} | {self.preco_fabrica} | {self.preco_venda}'

    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria

    @property
    def estoque(self):
        return self._estoque

    @property
    def preco_fabrica(self):
        return self._preco_fabrica

    @property
    def preco_venda(self):
        return self._preco_venda

    @classmethod
    def exibir_estoque(self):
        print('Exibindo estoque da Farmácia \n')
        print(f'{"Nome do Produto".ljust(20)}|{"Categoria".ljust(20)}|{"Tarja".ljust(20)}|{"Custo".ljust(20)}|{"Preço".ljust(20)}|{"Estoque"}')
        for i, produto in enumerate(self.produtos, start=1):
            if hasattr(produto, 'tarja'):
                print(f'{produto.nome.ljust(20)}|{produto.categoria.ljust(20)}|{self._tarja.ljust(20)}|{str(produto.preco_fabrica).ljust(20)}|{str(produto.preco_venda).ljust(20)}|{produto.estoque} unidades em estoque.')
            else:
                 print(f'{produto.nome.ljust(20)}|{produto.categoria.ljust(20)}|{'N/A'.ljust(20)}|{str(produto.preco_fabrica).ljust(20)}|{str(produto.preco_venda).ljust(20)}|{produto.estoque} unidades em estoque.')

    def registrar_entrada(self, qtde):
        self._estoque += qtde
