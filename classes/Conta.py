from __future__ import annotations
from rich import print
from decimal import Decimal
from random import random, randint
from typing import TYPE_CHECKING

from classes.Historico import Historico

if TYPE_CHECKING:
    from classes.Cliente import Cliente

class Conta:
    def __init__(self, numero: int, cliente: Cliente):
        self._saldo = Decimal(0)
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self) -> Decimal:
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
    def nova_conta(cls, cliente: Cliente):
        numero = randint(1, 9999)
        return cls(numero, cliente)

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            saldo:\t\t{self.saldo:.2f}
        """

    def sacar(self, valor: Decimal) -> bool:
        if valor > 0:
            if self.saldo >= valor:
                self._saldo -= valor
                return True
            else:
                print(f"Não foi possível realizar a operação. Saldo insuficiente.")
                print(f"Saldo: {self._saldo:.2f}")
                return False
        else:
            print(f"Não foi possível realizar a operação.  O valor informado é inválido.")
            return False
    def depositar(self, valor: Decimal) -> bool:
        if valor > 0:
            self._saldo += valor
            return True

        print("Operação falhou! O valor informado é inválido.")
        return False