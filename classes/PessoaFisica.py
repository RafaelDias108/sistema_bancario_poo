from classes.Cliente import Cliente
from datetime import date

class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str):
        super().__init__(nome, endereco)
        self.cpf = cpf
        self.data_nascimento = data_nascimento