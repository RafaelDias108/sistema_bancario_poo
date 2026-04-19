from __future__ import annotations
from classes.Transacao import Transacao
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classes.Conta import Conta

class Cliente:
    def __init__(self, nome: str, endereco: str):
        self._nome = nome
        self._endereco = endereco
        self._contas: list[Conta] = []

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def endereco(self) -> str:
        return self._endereco

    @property
    def contas(self) -> list:
        return self._contas

    @staticmethod
    def realizar_transacao(conta: Conta, transacao: Transacao):
        return transacao.registrar(conta=conta)

    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)