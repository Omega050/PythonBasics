from modelos.produto import Produto
from datetime import datetime

class Receita:
    receitas = []

    def __init__(self, medicamento, paciente, medico, tipo, data):
        self._medicamento = medicamento
        self._paciente = paciente 
        self._medico = medico
        self._tipo = tipo
        self._data = data
        self.status = True
        Receita.receitas.append(self)

    @property
    def status(self):
        return 'Receita Válida' if self.status else 'Inválida'
    
    @staticmethod
    def verificar_receitas():
        data_atual = datetime.now()
        for receita in Receita.receitas:
            if receita._data < data_atual:
                print(f"A receita para {receita._paciente} está vencida.")
            else:
                print(f"A receita para {receita._paciente} está válida.")

