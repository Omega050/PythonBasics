class Pessoa:
    def __init__(self='', nome='', idade=0, cpf=0):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
    
    def saudacao(self):
        print(f'Olá, eu me chamo {self._nome}, tenho {self._idade} anos')
    def aniversario(self):
        self._idade+=1
    
pessoa1 = Pessoa('André', 25, 33333)
pessoa1.aniversario()
pessoa1.saudacao()