import Transacao, Conta


class Cliente:
    def __init__(self, endereco: str):
        self._endereco = endereco
        self._contas: list = []

    @property
    def endereco(self) -> str:
        return self._endereco

    @property
    def contas(self) -> list:
        return self._contas

    @staticmethod
    def realizar_transacao(conta: Conta, transacao: Transacao):
        transacao.registrar(conta=conta)

    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)