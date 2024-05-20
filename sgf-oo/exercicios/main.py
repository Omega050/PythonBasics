from livro import Livro
livro1=Livro('O Príncipe', 'Maquiavel', 1854)
livro2=Livro('O Príncipe 2', 'Cleber', 2424)
livro3=Livro('O Príncipe 3', 'Cleber', 2424)
livro4=Livro('O Príncipe 4', 'Cleber', 2424)
livro5=Livro('O Príncipe 5', 'Cleber', 2424)
livro1.emprestar()
livro3.emprestar()

Livro.verificar(2424)
print(livro1)
print(livro2)