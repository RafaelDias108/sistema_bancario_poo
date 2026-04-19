import Cliente


class Conta:
    def __init__(self, numero: int, cliente: Cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self) -> float:
        return self._saldo
    @property
    def numero(self) -> int:
        return self._numero
    @property
    def agencia(self) -> str:
        return self._agencia
    @property
    def cliente(self) -> Cliente:
        return self._cliente
    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int):
        return cls(numero, cliente)

    def sacar(self, valor: float) -> bool:
        pass

    def depositar(self, valor: float) -> bool:
        pass