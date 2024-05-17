from modelos.produto import Produto

prod1= Produto('Durateston', 'Bomba', 10, 15)
prod2= Produto('Trembo', 'SemReceita', 20, 200)

def main():
    Produto.exibir_estoque()

if __name__ == '__main__':
    main()