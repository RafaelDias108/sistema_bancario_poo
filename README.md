# Sistema Bancário com Python Orientado a Objetos

Este projeto foi desenvolvido como parte do desafio **"Modelando o Sistema Bancário em POO com Python"**, integrante do **Bootcamp Luizalabs - Back-end com Python (2ª Edição)** da [DIO](https://www.dio.me/).

## 📌 Objetivo do Projeto

O objetivo deste desafio foi aplicar os conceitos de Programação Orientada a Objetos (POO) em Python para modelar um sistema bancário funcional. A implementação segue o diagrama de classes UML fornecido durante o treinamento, focando em:

- **Abstração:** Representação de entidades do mundo real (Clientes, Contas, Transações).
- **Encapsulamento:** Proteção de dados sensíveis e lógica interna das classes.
- **Herança:** Especialização de classes (ex: `PessoaFisica` herdando de `Cliente`).
- **Polimorfismo:** Implementação do método `registrar` em diferentes tipos de transações.

## 🏗️ Arquitetura do Sistema

O sistema está organizado em módulos dentro da pasta `classes/`, seguindo a seguinte estrutura:

- **Cliente:** Classe base para os clientes do banco.
- **PessoaFisica:** Especialização de cliente com CPF e data de nascimento.
- **Conta:** Classe base para as contas bancárias (Depósito, Saque, Saldo).
- **ContaCorrente:** Especialização de conta com limites de saque e saldo extra.
- **Historico:** Registro de todas as transações realizadas.
- **Transacao:** Interface (classe abstrata) para as operações.
- **Saque e Deposito:** Implementações concretas das transações.
- **SistemaBancario:** Classe que gerencia a interface com o usuário e as operações de negócio.

### 📊 Diagrama UML
O projeto inclui o diagrama de classes original (`UML Desafio.png`) que serviu como guia para a modelagem técnica.

## 🚀 Tecnologias Utilizadas

- **Python 3.12+**
- **POO (Programação Orientada a Objetos)**

## 🛠️ Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone o repositório:
   ```bash
   git clone git@github.com:RafaelDias108/sistema_bancario_poo.git
   ```
3. Navegue até o diretório do projeto:
   ```bash
   cd sistema_bancario_poo
   ```
4. Execute o script principal:
   ```bash
   python main.py
   ```

## 📝 Licença

Este projeto é de fins educacionais e segue as diretrizes do bootcamp da DIO.

---
Desenvolvido por [Rafael Dias](https://github.com/RafaelDias108).
