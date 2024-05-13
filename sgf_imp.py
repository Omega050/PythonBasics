import os, sys

produtos = [{'nome':'Dipirona', 'categoria':'Analgésico', 'estoque':32},
            {'nome':'Toragesik', 'categoria':'Não Sei', 'estoque':12},
            {'nome':'Durateston', 'categoria':'BOMBA', 'estoque':5},  
            {'nome':'Trembo', 'categoria':'SemReceita', 'estoque':0}         
            ]

def menu():
    print ("""
    SGF - Sistema de Gerenciamento de Farmácias\n
    """)
    print ('1 - Realizar Venda')
    print ('2 - Modificar Estoque')
    print ('3 - Cadastrar Produto')
    print ('4 - Visualizar Estoque')
    print ('5 - Encerrar\n')

def inicia_funcao(mensagem_inicial):
    os.system('cls')
    linha = '**' +'*' * (len(mensagem_inicial))+'**'
    print(linha)
    print(f'  {mensagem_inicial}')
    print(linha)
    print('\n')

def invalid_op():
    inicia_funcao('Opção Inválida')
    voltar_ao_menu()

def invalid_op_m():
    inicia_funcao('Opção Inválida')
    input()
    modifica_estoque()

def voltar_ao_menu():
    c=input("""Deseja voltar ao menu Principal?
               
    S/N
    """)
    if c=='S':
        main()
    elif c=='N':
        sys.exit()
    else:
        invalid_op()

def registra_entrada(): 
    '''Realiza adição de unidades em estoque ao produto se este estiver cadastrado, caso contrário, direciona para uma funçaõ de cadastro
       Inputs: Nome do produto a ser alterado,
               Quantidade a ser adicionada
               Opção de cadastrar ou não o produto não encontrado
       
       Outputs: Estoque do produto modificado

    '''
    modificar_produto = input('Qual o nome do produto dar entrada? ')
    produto_encontrado=False
    for produto in produtos:
        if modificar_produto==produto['nome']:
            produto_encontrado=True
            quantidade_adicionada=int(input('Quantas unidades deseja adicionar? '))
            produto['estoque']+=quantidade_adicionada
            voltar_ao_menu()
                                   
    if not produto_encontrado:
        produto_nao_cadastrado=input('Produto não encontrado, deseja realizar o cadastro?')
        print('(S/N)')
        if produto_nao_cadastrado=='S':
            cadastrar_produto_n(modificar_produto)
        elif produto_nao_cadastrado=='N':
            modifica_estoque()
        else:
            invalid_op_m()

def corrige_estoque():
    corrigir_produto = input('Qual o nome do produto corrigir? ')
    produto_encontrado=False
    for produto in produtos:
        if corrigir_produto==produto['nome']:
            produto_encontrado=True
            print(f'O produto {produto["nome"]} possui {produto["estoque"]} unidades cadastradas')
            estoque_corrigido=int(input(f'Quantas unidades o produto {produto["nome"]} realmente tem em estoque? '))
            produto['estoque']=estoque_corrigido
            voltar_ao_menu()
                                   
    if not produto_encontrado:
        produto_nao_cadastrado=input('Produto não encontrado, deseja realizar o cadastro?')
        print('(S/N)')
        if produto_nao_cadastrado=='S':
            cadastrar_produto_n(corrigir_produto)
        elif produto_nao_cadastrado=='N':
            modifica_estoque()
        else:
            invalid_op_m()

def modifica_estoque():
    inicia_funcao('Modificando o Estoque')
    visualiza_estoque()
    try:
        op_modificacao= int(input("""O que deseja fazer?
    1- Registrar entrada
    2- Corrigir quantidade em estoque
    3- Voltar ao menu
    """))
        match op_modificacao:
            case 1:
                registra_entrada()
            case 2:
                corrige_estoque()
            case 3: 
                main()
            case _:
                invalid_op_m()
    except:
        invalid_op_m()

def cadastrar_produto():
    '''Realiza o cadastro de um novo produto no estoque
       Inputs: Nome do Produto,
               Categoria do Produto
       Outputs: Produto criado
    '''
    inicia_funcao('Cadastro de novo Produto')
    produto_nome = input ('Digite o nome do produto que deseja cadastrar ')
    produto_categoria=input(f'Digite a categoria do produto {produto_nome} ')
    produto={'nome':produto_nome, 'categoria':produto_categoria, 'estoque':0}
    produtos.append(produto)
    voltar_ao_menu()

def cadastrar_produto_n(modificar_produto):
    '''Similar ao anterior, porém por ser chamado por outra função, possui o nome como parametro e permite o cadastro de quantidade
       Inputs: Categoria do Produto,
               Quantidade em Estoque
       Outputs: Produto criado
    
    '''
    inicia_funcao('Cadastro de novo Produto')
    produto_nome = modificar_produto
    produto_categoria=input(f'Digite a categoria do produto {produto_nome} ')
    produto_estoque=int(input(f'Quantas unidades o produto {produto_nome} possui em estoque? '))
    produto={'nome':produto_nome, 'categoria':produto_categoria, 'estoque':produto_estoque}
    produtos.append(produto)
    voltar_ao_menu()

def visualiza_estoque():
    '''Exibe os produtos cadastrados, bem como suas respectivas categorias e quantidades
       Inputs: any
       Outputs: Lista contendo os produtos
    
    '''
    print(f'{"Nome do Produto".ljust(20)}|{"Categoria do Produto".ljust(20)}|Estoque')
    for produto in produtos:
        nome_produto=produto['nome']
        categoria_produto=produto['categoria']
        estoque_produto=produto['estoque']
        print(f'{nome_produto.ljust(20)}|{categoria_produto.ljust(20)}|{estoque_produto} unidades em estoque.')
    print()

def so_visualiza_estoque():
    '''Executa a função de visualizar o estoque de forma isolada'''
    inicia_funcao('Visualizando Estoque')
    visualiza_estoque()
    input()
    voltar_ao_menu()

def op_list():
    try:
           op=int(input('Escolha uma opção\n'))
           match op:
              case 1:
                     print(1)
              case 2:
                     modifica_estoque()
              case 3:
                     cadastrar_produto()
              case 4:
                     so_visualiza_estoque()
              case 5:
                     print('Encerrando')
              case _:
                     invalid_op()
    except:
        invalid_op()

def main():
    os.system('cls')
    menu ()
    op_list()

if __name__ == '__main__':
    main()  
