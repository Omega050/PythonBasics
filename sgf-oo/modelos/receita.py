from datetime import datetime, timedelta
class Receita:
    receitas = []

    def __init__(self, medicamento, cliente, medico, tipo, data):
        self._medicamento = medicamento
        self._cliente = cliente
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