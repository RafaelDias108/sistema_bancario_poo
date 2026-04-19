import textwrap
from datetime import datetime
from decimal import Decimal
from time import sleep

from rich.panel import Panel
from rich import print

from classes.ContaCorrente import ContaCorrente
from classes.Deposito import Deposito
from classes.PessoaFisica import PessoaFisica
from classes.Saque import Saque


class SistemaBancario:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def menu(self):
        opcoes = """[white]
        [1]\tDepositar
        [2]\tSacar
        [3]\tExtrato
        [4]\tNova conta
        [5]\tListar contas
        [6]\tNovo cliente
        [0]\tSair
        """
        painel = Panel(opcoes, title="MENU DO SISTEMA", width=40, style='bold', border_style="blue")
        print(painel)
        return input(textwrap.dedent("Digite a opção => "))

    def depositar(self):
        cpf = input("Digite seu CPF: ").strip()
        if not cpf or len(cpf) == 0:
            print(Panel("CPF não informado.", title="Notificação", border_style="red", width=40))
            return

        cliente = self.filtrar_cliente(cpf=cpf)
        if not cliente:
            print(Panel("Cliente não encontrado.", title="Notificação", border_style="red", width=40))
            return

        valor = input("Digite o valor do depósito: ").strip()
        if len(valor) == 0:
            print(Panel("Valor do depósito não informado.", title="Notificação", border_style="red", width=40))
            return

        transacao = Deposito(valor=Decimal(valor))

        conta = self.pegar_conta_cliente(cliente=cliente)
        if conta is None:
            print(Panel("Conta não encontrado.", title="Notificação", border_style="red", width=40))
            return

        transacao_realizada = cliente.realizar_transacao(conta=conta, transacao=transacao)

        if transacao_realizada:
            transacao = conta.historico.transacoes[-1]

            tipo = transacao.get('tipo')
            valor = transacao.get('valor')
            valor_formatado = f"{valor:.2f}" if valor else None
            data_transacao = transacao.get('data')

            extrato = Panel("", title=f"Transação {tipo}", border_style="blue", width=80)
            extrato.renderable += f"Tipo: {tipo} - Valor: {valor_formatado} Data e hora: {data_transacao}\n"
            extrato.renderable += f"Saldo: {Decimal(conta.saldo):.2f}"
            print(extrato)

    def sacar(self):
        cpf = input("Digite seu CPF: ").strip()
        if not cpf or len(cpf) == 0:
            print(Panel("CPF não informado.", title="Notificação", border_style="red", width=40))
            return

        cliente = self.filtrar_cliente(cpf=cpf)
        if not cliente:
            print(Panel("Cliente não encontrado.", title="Notificação", border_style="red", width=40))
            return

        valor = input("Digite o valor do saque: ").strip()
        if len(valor) == 0:
            print(Panel("Valor do saque não informado.", title="Notificação", border_style="red", width=40))
            return

        transacao = Saque(valor=Decimal(valor))

        conta = self.pegar_conta_cliente(cliente=cliente)
        if conta is None:
            print(Panel("Conta não encontrado.", title="Notificação", border_style="red", width=40))
            return

        transacao_realizada = cliente.realizar_transacao(conta=conta, transacao=transacao)

        if transacao_realizada:
            transacao = conta.historico.transacoes[-1]

            tipo = transacao.get('tipo')
            valor = transacao.get('valor')
            valor_formatado = f"{valor:.2f}" if valor else None
            data_transacao = transacao.get('data')

            extrato = Panel("", title=f"Transação {tipo}", border_style="blue", width=80)
            extrato.renderable += f"Tipo: {tipo} - Valor: {valor_formatado} Data e hora: {data_transacao}\n"
            extrato.renderable += f"Saldo: {Decimal(conta.saldo):.2f}"
            print(extrato)


    def pegar_conta_cliente(self, cliente: PessoaFisica) -> ContaCorrente:
        if not cliente.contas:
            return None

        if len(cliente.contas) > 1:
            for conta in cliente.contas:
                print(Panel(textwrap.dedent(str(conta)), title="Conta", border_style="green", width=50))
            numero_conta =  input(textwrap.dedent("Digite o número da conta que deseja acessar => "))

            for conta in cliente.contas:
                if conta.numero == int(numero_conta):
                    return conta

        return cliente.contas[0]

    def extrato(self):
        cpf = input("Digite seu CPF: ").strip()
        if not cpf or len(cpf) == 0:
            print(Panel("CPF não informado.", title="Notificação", border_style="red", width=40))
            return

        cliente = self.filtrar_cliente(cpf=cpf)
        if not cliente:
            print(Panel("Cliente não encontrado.", title="Notificação", border_style="red", width=40))
            return

        conta = self.pegar_conta_cliente(cliente)
        if not conta:
            print(Panel("Conta não encontrado.", title="Notificação", border_style="red", width=40))
            return

        transacoes = conta.historico.transacoes
        extrato = Panel("", title="Extrato", border_style="blue", width=80)
        extrato.title += f" da conta {conta.numero}"
        if len(transacoes) == 0:
            extrato.renderable = "Não foram realizadas movimentações."
        else:
            for transacao in transacoes:

                tipo = transacao.get('tipo')
                valor = transacao.get('valor')
                valor_formatado = f"{valor:.2f}" if valor else None
                data_transacao = transacao.get('data')

                extrato.renderable += f"Tipo: {tipo} - Valor: {valor_formatado} Data e hora: {data_transacao}\n\n"

            extrato.renderable += f"\nSaldo: {Decimal(conta.saldo):.2f}"

        print(extrato)

    def listar_contas(self):
        for conta in self.contas:
            print(Panel(textwrap.dedent(str(conta)), title="Conta", border_style="green", width=50))

    def nova_conta(self):
        cpf = input("Digite seu CPF: ").strip()

        if not cpf:
            print("Necessário informar o cpf")
            return

        cliente = self.filtrar_cliente(cpf=cpf)
        if not cliente:
            print("[red]Cliente não encontrado, fluxo de criação de conta encerrado!")
            return

        conta = ContaCorrente.nova_conta(cliente=cliente)
        self.contas.append(conta)
        cliente.contas.append(conta)

        print(Panel(f"Conta número: {conta.numero} criada com sucesso!", title="Conta criada", border_style="green", width=40))

    def filtrar_cliente(self, cpf: str) -> PessoaFisica:
        clientes_filtrados = [cliente for cliente in self.clientes if cliente.cpf == cpf]
        return clientes_filtrados[0] if clientes_filtrados else None

    def novo_cliente(self):
        cpf = input("Digite seu CPF: ").strip()
        if not cpf or len(cpf)  == 0:
            print("[yellow]Necessário informar o cpf")
            return
        cliente = self.filtrar_cliente(cpf=cpf)

        if cliente:
            print(Panel("[white]Já existe cliente com o CPF informado !", title="Notificação", border_style="red", width=50))
            return

        nome = input("Digite seu nome: ").strip()
        data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ").strip()
        endereco = input("Informe seu endereço. (Ex: logradouro, número - bairro - cidade/uf): ").strip()

        try:
            data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
        except ValueError:
            print("[red]Formato de data inválido! Use dd/mm/aaaa.[/]")
            return

        cliente = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)
        self.clientes.append(cliente)

        dados_cliente = f"""
        Nome do cliente: {cliente.nome}
        CPF: {cliente.cpf}
        Data de nascimento: {cliente.data_nascimento.strftime('%d/%m/%Y')}
        Endereço: {cliente.endereco}
        """
        print(Panel(dados_cliente, title="Cliente criado com sucesso", border_style="green", width=60))

    def run(self):
        while True:
            opcao = self.menu()

            match opcao:
                case '1':
                    print("[bold blue]==== Sistema Bancario - [1] Depositar ====")
                    self.depositar()
                    sleep(1)
                case '2':
                    print("[bold blue]==== Sistema Bancario - [2] Sacar ====")
                    self.sacar()
                    sleep(1)
                case '3':
                    print("[bold blue]==== Sistema Bancario - [3] Extrato ====")
                    self.extrato()
                    sleep(1)
                case '4':
                    print("[bold blue]==== Sistema Bancario - [4] Nova conta ====")
                    self.nova_conta()
                    sleep(1)
                case '5':
                    print("[bold blue]==== Sistema Bancario - [5] Listar Contas ====")
                    self.listar_contas()
                    sleep(1)
                case '6':
                    print("[bold blue]==== Sistema Bancario - [6] Novo cliente ====")
                    self.novo_cliente()
                    sleep(1)
                case '0':
                    print("Saindo do programa...")
                    sleep(1)
                    break
                case _:
                    print("[red]Operação inválida, por favor selecione novamente a operação desejada.[/] :")
                    sleep(1)
