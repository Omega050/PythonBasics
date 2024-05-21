from veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas=portas

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Portas: {self.portas} | Estado: {status}'