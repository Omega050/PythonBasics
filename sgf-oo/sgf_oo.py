from modelos.produto import Produto
from modelos.receita import Receita
from modelos.cliente import Cliente
from modelos.medicamento import Medicamento
from datetime import datetime

prod1= Medicamento('Durateston', 'Bomba', 'Preta', 10, 15)
prod2= Produto('Trembo', 'SemReceita', 20, 200)

cliente1 = Cliente('Paulo', '3212312')

receita1 = Receita(prod1, cliente1, "Dr. Maria", "Simples", datetime(2024, 5, 5))
Cliente.registra_receita(cliente1, receita1)


def main():
    Produto.exibir_estoque()
    Receita.verificar_receitas()
    for receita in Receita.receitas:
        data_formatada = receita._data.strftime("%Y-%m-%d")
        print(f"Medicamento: {receita._medicamento.nome}, Paciente: {receita._cliente.nome}, Tipo: {receita._tipo}, Data: {data_formatada}, Status: {receita.status}")

if __name__ == '__main__':
    main()