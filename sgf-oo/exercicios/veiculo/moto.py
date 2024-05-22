from veiculo import Veiculo
class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Tipo: {self.tipo} | Estado: {status}'
    
    def ligar(self):
        self._ligado = not self._ligado
        print(f'Ligando a moto')