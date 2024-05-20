from modelos.produto import Produto
from modelos.receita import Receita
from datetime import datetime

prod1= Produto('Durateston', 'Bomba', 10, 15)
prod2= Produto('Trembo', 'SemReceita', 20, 200)


receita1 = Receita(prod1, "João", "Dr. Maria", "Controle", datetime(2024, 5, 15))
receita2 = Receita(prod2, "Maria", "Dr. José", "Urgência", datetime(2024, 5, 20))



def main():
    Produto.exibir_estoque()
    Receita.verificar_receitas()

if __name__ == '__main__':
    main()