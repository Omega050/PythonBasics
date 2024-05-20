class Conta_bancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        
    
    def __str__(self):
        return f'{self._titular.ljust(20)} || R${str(self._saldo).ljust(20)} || {self.ativo}'
    
    def ativar_conta(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativo'

conta1=Conta_bancaria('Mauro', 100000)
conta1.ativar_conta()
conta2=Conta_bancaria('Duda', 50000)

print(conta1)
print(conta2)