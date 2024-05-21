class Cliente:
    def __init__(self, nome, cpf):
        self._nome=nome
        self._cpf = cpf
        self._receitas = []

    def registra_receita(self, receita):
        self._receitas.append(receita)

    @property
    def nome(self):
        return self._nome


    