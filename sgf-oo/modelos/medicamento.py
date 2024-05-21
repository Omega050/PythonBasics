from modelos.produto import Produto
class Medicamento (Produto):
    def __init__(self, nome, categoria, tarja, preco_f, preco_v):
        super().__init__(nome, categoria, preco_f, preco_v)
        self._tarja = tarja