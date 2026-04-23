from decimal import Decimal
from rich.panel import Panel
from rich import print

from classes.Cliente import Cliente
from classes.Conta import Conta
from classes.Saque import Saque


class ContaCorrente(Conta):
    def __init__(self,  numero: int, cliente: Cliente, limite: Decimal = 1000, limite_saques: int = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor: Decimal):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            panel = Panel(renderable=f"Operação falhou: O valor de saque excedeu o limite de {self._limite:.2f}", title="Notificação", border_style="red", width=50)
            print(panel)
        elif excedeu_saques:
            panel = Panel(renderable="Operação falhou: número máximo de saques excedido", title="Notificação", border_style="red", width=50)
            print(panel)
        else:
            return super().sacar(valor=valor)

        return False