class Produto:
    produtos = []
    def __init__(self, nome, categoria, preco_f, preco_v):
        self.nome = nome
        self.categoria = categoria
        self.estoque = 0
        self.preco_fabrica=preco_f
        self.preco_venda=preco_v
        Produto.produtos.append(self)
    
    def __str__(self): # get nome
        return f'{self.nome} | {self.categoria} | {self.estoque} | {self.preco_fabrica} | {self.preco_venda}'
    
    def exibir_estoque():
        print(f'{'Nome do Produto'.ljust(20)}|{'Categoria'.ljust(20)}|{'Custo'.ljust(20)}|{'Preço'.ljust(20)}Estoque')
        for produto in Produto.produtos:
            print(f'{produto.nome.ljust(20)}|{produto.categoria.ljust(20)}|{str(produto.preco_fabrica).ljust(20)}|{str(produto.preco_venda).ljust(20)}|{produto.estoque} unidades em estoque.')
        print()
    
prod1= Produto('Durateston', 'Bomba', 10, 15)
prod2= Produto('Trembo', 'SemReceita', 20, 200)
Produto.exibir_estoque()