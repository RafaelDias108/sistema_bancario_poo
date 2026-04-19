from decimal import Decimal

from classes.Conta import Conta
from classes.Transacao import Transacao


class Deposito(Transacao):

    def __init__(self, valor: Decimal):
        self._valor = valor

    @property
    def valor(self) -> Decimal:
        return self._valor

    def registrar(self, conta: Conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

        return sucesso_transacao