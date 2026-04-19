from __future__ import annotations
from abc import ABC, abstractmethod
from decimal import Decimal
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classes.Conta import Conta


class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self) -> Decimal:
        pass

    @abstractmethod
    def registrar(self, conta: Conta):
        pass