from __future__ import annotations

from decimal import Decimal
from typing import TYPE_CHECKING

from classes.Transacao import Transacao

if TYPE_CHECKING:
    from classes.Conta import Conta

class Saque(Transacao):

    def __init__(self, valor: Decimal):
        self._valor = valor

    @property
    def valor(self) -> Decimal:
        return self._valor

    def registrar(self, conta: Conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

        return sucesso_transacao