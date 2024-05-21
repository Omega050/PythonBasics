from datetime import datetime, timedelta

class Produto:
    produtos = []

    def __init__(self, nome, categoria, preco_f, preco_v):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._estoque = 0
        self._preco_fabrica = preco_f
        self._preco_venda = preco_v
        self._precisa_de_receita = False
        Produto.produtos.append(self)

    def __str__(self):  # get nome
        return f'{self.nome} | {self.categoria} | {self.estoque} | {self.preco_fabrica} | {self.preco_venda}'

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
    def exibir_estoque(cls):
        print(f'{"Nome do Produto".ljust(20)}|{"Categoria".ljust(20)}|{"Custo".ljust(20)}|{"Preço".ljust(20)}|{"Estoque"}')
        for produto in cls.produtos:
            print(f'{produto.nome.ljust(20)}|{produto.categoria.ljust(20)}|{str(produto.preco_fabrica).ljust(20)}|{str(produto.preco_venda).ljust(20)}|{produto.estoque} unidades em estoque.')
        print()

    def registrar_entrada(self, qtde):
        self._estoque += qtde

class Receita:
    receitas = []

    def __init__(self, medicamento, paciente, medico, tipo, data):
        self._medicamento = medicamento
        self._paciente = paciente
        self._medico = medico
        self._tipo = tipo
        self._data = data
        self._status = True
        Receita.receitas.append(self)

    @property
    def status(self):
        return 'Receita Válida' if self._status else 'Inválida'

    @status.setter
    def status(self, value):
        self._status = value

    @staticmethod
    def verificar_receitas():
        data_atual = datetime.now()
        for receita in Receita.receitas:
            if not receita._status:
                continue
            elif (receita._tipo == 'Simples' or receita._tipo == 'Controle Especial') and receita._data + timedelta(days=30) < data_atual:
                receita._status = False
            elif receita._tipo == 'Antimicrobiana' and receita._data + timedelta(days=10) < data_atual:
                receita._status = False

# Exemplo de uso
produto1 = Produto("Paracetamol", "Analgésico", 10.50, 15.00)
produto2 = Produto("Dipirona", "Analgésico", 8.75, 12.00)

produto1.registrar_entrada(50)
produto2.registrar_entrada(30)

Produto.exibir_estoque()

# Criação de receitas para teste
receita1 = Receita(produto1, "João", "Dr. Maria", "Simples", datetime(2024, 4, 1))
receita2 = Receita(produto2, "Maria", "Dr. José", "Antimicrobiana", datetime(2024, 5, 10))
receita3 = Receita(produto1, "Carlos", "Dr. Ana", "Controle Especial", datetime(2024, 3, 20))
receita4 = Receita(produto2, "Ana", "Dr. Paulo", "Simples", datetime(2024, 1, 15))

# Verificação das receitas
Receita.verificar_receitas()

# Verificação dos resultados
for receita in Receita.receitas:
    data_formatada = receita._data.strftime("%Y-%m-%d")
    print(f"Medicamento: {receita._medicamento.nome}, Paciente: {receita._paciente}, Tipo: {receita._tipo}, Data: {data_formatada}, Status: {receita.status}")
