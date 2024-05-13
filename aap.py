import os, sys
produtos = ['Dipirona','Toragesik', 'Durateston']
def menu():
       print ("""
SGF - Sistema de Gerenciamento de Farmácias\n
       """)
       print ('1 - Realizar Venda')
       print ('2 - Registrar Entrada')
       print ('3 - Cadastrar Produto')
       print ('4 - Visualizar Vendas')
       print ('5 - Encerrar\n')

def inicia_funcao(mensagem_inicial):
      os.system('cls')
      print(mensagem_inicial)
      print('\n')

def invalid_op():
       inicia_funcao('Opção Inválida')
       c=input("""Deseja voltar ao menu Principal?
               
S/N
""")
       if c=='S':
              main()
       elif c=='N':
              sys.exit()


def cadastrar_produto():
      inicia_funcao('Cadastro de novo Produto')
      produto = input ('Digite o nome do produto que deseja cadastrar ')
      produtos.append(produto)

def listar_produtos():
      inicia_funcao('Listando Produtos')
      for produto in produtos:
              print(produto)
              print('\n')
def op_list():
       try:
              op=int(input('Escolha uma opção\n'))
              print(f'Você escolheu a opção {op}')
              match op:
                case 1:
                     print(1)
                case 2:
                     print(2)
                case 3:
                     cadastrar_produto()
                case 4:
                     listar_produtos()
                case 5:
                     print('Encerrando')
                case _:
                     invalid_op()
       except:invalid_op()

def main():
       os.system('cls')
       menu ()
       op_list()
if __name__ == '__main__':
       main()  

