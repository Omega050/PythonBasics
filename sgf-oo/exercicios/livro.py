class Livro():
    livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)
    
    def __str__(self):
        return f'O livro {self._titulo} foi escrito por {self._autor} e foi publicado no ano de {self._ano_publicacao}'

    def emprestar(self):
        self._disponivel = not self._disponivel

    @property
    def disponivel(self):
        return 'Disponível' if self._disponivel else 'Indisponível'
    
    @classmethod
    def verificar(cls, ano):
        for livro in cls.livros:
            if livro._ano_publicacao == ano and livro._disponivel:
                print(f'{livro._titulo}, {livro.disponivel}')

