from classes.Cliente import Cliente
from classes.Conta import Conta


class ContaCorrente(Conta):
    def __init__(self,  numero: int, cliente: Cliente, limite: float = 500, limite_saques: int = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
