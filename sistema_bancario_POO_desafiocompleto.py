from abc import ABC, abstractmethod
from datetime import datetime
import re


class Transacao(ABC):
    """Interface para transações bancárias"""
    
    @abstractmethod
    def registrar(self, conta):
        """Registra a transação na conta"""
        pass


class Deposito(Transacao):
    """Classe para operações de depósito"""
    
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        """Registra o depósito na conta"""
        sucesso = conta.depositar(self._valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    """Classe para operações de saque"""
    
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        """Registra o saque na conta"""
        sucesso = conta.sacar(self._valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


class Historico:
    """Classe para armazenar o histórico de transações"""
    
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        """Adiciona uma transação ao histórico"""
        self._transacoes.append({
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        })


class Conta:
    """Classe base para contas bancárias"""
    
    def __init__(self, numero, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        """Método de classe para criar nova conta"""
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        """Realiza saque da conta"""
        if valor <= 0:
            print("❌ Valor inválido! O valor deve ser positivo.")
            return False
        
        if valor > self._saldo:
            print("❌ Saldo insuficiente para realizar o saque.")
            print(f"Seu saldo atual é de R$ {self._saldo:.2f}")
            return False
        
        self._saldo -= valor
        print("✅ Saque realizado com sucesso!")
        print(f"Valor sacado: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {self._saldo:.2f}")
        return True
    
    def depositar(self, valor):
        """Realiza depósito na conta"""
        if valor <= 0:
            print("❌ Valor inválido! O valor deve ser positivo.")
            return False
        
        self._saldo += valor
        print("✅ Depósito realizado com sucesso!")
        print(f"Valor depositado: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {self._saldo:.2f}")
        return True


class ContaCorrente(Conta):
    """Classe para conta corrente com limite de saque"""
    
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        self._saques_realizados = 0
    
    @property
    def limite(self):
        return self._limite
    
    @property
    def limite_saques(self):
        return self._limite_saques
    
    @property
    def saques_realizados(self):
        return self._saques_realizados
    
    def sacar(self, valor):
        """Sobrescreve o método sacar com validações específicas"""
        if self._saques_realizados >= self._limite_saques:
            print("❌ Limite de saques diários atingido!")
            print(f"Você já realizou {self._saques_realizados} saques hoje.")
            return False
        
        if valor > self._limite:
            print(f"❌ Valor excede o limite de saque de R$ {self._limite:.2f}")
            return False
        
        sucesso = super().sacar(valor)
        if sucesso:
            self._saques_realizados += 1
            print(f"Saques restantes hoje: {self._limite_saques - self._saques_realizados}")
        
        return sucesso
    
    def __str__(self):
        return f"""
        Agência: {self.agencia}
        C/C: {self.numero}
        Titular: {self.cliente.nome}
        Saldo: R$ {self.saldo:.2f}
        Limite Saque: R$ {self.limite:.2f}
        Saques Realizados: {self.saques_realizados}/{self.limite_saques}
        """


class PessoaFisica:
    """Classe para pessoa física"""
    
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._endereco = endereco
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def endereco(self):
        return self._endereco


class Cliente:
    """Classe para cliente do banco"""
    
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
    
    @property
    def endereco(self):
        return self._endereco
    
    @property
    def contas(self):
        return self._contas
    
    def realizar_transacao(self, conta, transacao):
        """Realiza uma transação em uma conta específica"""
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        """Adiciona uma conta ao cliente"""
        self._contas.append(conta)


class PessoaFisicaCliente(PessoaFisica, Cliente):
    """Classe que herda de PessoaFisica e Cliente"""
    
    def __init__(self, nome, data_nascimento, cpf, endereco):
        PessoaFisica.__init__(self, nome, data_nascimento, cpf, endereco)
        Cliente.__init__(self, endereco)


class SistemaBancario:
    """Classe principal do sistema bancário"""
    
    def __init__(self):
        self._clientes = []
        self._contas = []
        self._numero_conta_sequencial = 1
    
    def validar_cpf(self, cpf):
        """Valida se o CPF tem formato correto"""
        return cpf.isdigit() and len(cpf) == 11
    
    def buscar_cliente_por_cpf(self, cpf):
        """Busca um cliente pelo CPF"""
        for cliente in self._clientes:
            if hasattr(cliente, 'cpf') and cliente.cpf == cpf:
                return cliente
        return None
    
    def criar_cliente(self):
        """Cria um novo cliente"""
        print("\n👤 CRIAR NOVO CLIENTE")
        print("-" * 30)
        
        nome = input("Digite o nome completo: ").strip()
        if not nome:
            print("❌ Nome não pode estar vazio!")
            return
        
        data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ").strip()
        if not re.match(r'\d{2}/\d{2}/\d{4}', data_nascimento):
            print("❌ Formato de data inválido! Use DD/MM/AAAA")
            return
        
        cpf = input("Digite o CPF (apenas números): ").strip()
        if not self.validar_cpf(cpf):
            print("❌ CPF inválido! Digite apenas 11 números.")
            return
        
        if self.buscar_cliente_por_cpf(cpf):
            print("❌ Já existe um cliente cadastrado com este CPF!")
            return
        
        # Coleta endereço
        print("\n📍 ENDEREÇO:")
        logradouro = input("Logradouro: ").strip()
        numero = input("Número: ").strip()
        bairro = input("Bairro: ").strip()
        cidade = input("Cidade: ").strip()
        sigla_estado = input("Sigla do Estado (ex: SP): ").strip().upper()
        
        if not all([logradouro, numero, bairro, cidade, sigla_estado]):
            print("❌ Todos os campos do endereço são obrigatórios!")
            return
        
        endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{sigla_estado}"
        
        # Cria o cliente
        cliente = PessoaFisicaCliente(nome, data_nascimento, cpf, endereco)
        self._clientes.append(cliente)
        
        print("✅ Cliente criado com sucesso!")
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
    
    def criar_conta_corrente(self):
        """Cria uma nova conta corrente"""
        print("\n🏦 CRIAR CONTA CORRENTE")
        print("-" * 30)
        
        if not self._clientes:
            print("❌ Nenhum cliente cadastrado! Crie um cliente primeiro.")
            return
        
        cpf = input("Digite o CPF do cliente: ").strip()
        if not self.validar_cpf(cpf):
            print("❌ CPF inválido! Digite apenas 11 números.")
            return
        
        cliente = self.buscar_cliente_por_cpf(cpf)
        if not cliente:
            print("❌ Cliente não encontrado!")
            return
        
        # Verifica se o cliente já possui conta
        if cliente.contas:
            print("❌ Este cliente já possui uma conta corrente!")
            return
        
        # Cria a conta
        conta = ContaCorrente.nova_conta(cliente, self._numero_conta_sequencial)
        self._contas.append(conta)
        cliente.adicionar_conta(conta)
        self._numero_conta_sequencial += 1
        
        print("✅ Conta corrente criada com sucesso!")
        print(f"Agência: {conta.agencia}")
        print(f"Conta: {conta.numero}")
        print(f"Titular: {cliente.nome}")
    
    def selecionar_conta(self):
        """Seleciona uma conta para operações"""
        if not self._contas:
            print("❌ Nenhuma conta cadastrada!")
            return None
        
        print("\n📋 CONTAS DISPONÍVEIS:")
        print("-" * 40)
        for i, conta in enumerate(self._contas):
            print(f"{i+1}. Ag: {conta.agencia} - Conta: {conta.numero} - {conta.cliente.nome}")
        
        try:
            escolha = int(input("\nSelecione o número da conta: ")) - 1
            if 0 <= escolha < len(self._contas):
                return self._contas[escolha]
            else:
                print("❌ Conta inválida!")
                return None
        except ValueError:
            print("❌ Entrada inválida!")
            return None
    
    def realizar_saque(self):
        """Realiza operação de saque"""
        print("\n💰 OPERAÇÃO DE SAQUE")
        print("-" * 25)
        
        conta = self.selecionar_conta()
        if not conta:
            return
        
        try:
            valor = float(input("Digite o valor do saque: R$ "))
        except ValueError:
            print("❌ Valor inválido! Digite um número válido.")
            return
        
        transacao = Saque(valor)
        conta.cliente.realizar_transacao(conta, transacao)
    
    def realizar_deposito(self):
        """Realiza operação de depósito"""
        print("\n💳 OPERAÇÃO DE DEPÓSITO")
        print("-" * 26)
        
        conta = self.selecionar_conta()
        if not conta:
            return
        
        try:
            valor = float(input("Digite o valor do depósito: R$ "))
        except ValueError:
            print("❌ Valor inválido! Digite um número válido.")
            return
        
        transacao = Deposito(valor)
        conta.cliente.realizar_transacao(conta, transacao)
    
    def exibir_extrato(self):
        """Exibe o extrato de uma conta"""
        conta = self.selecionar_conta()
        if not conta:
            return
        
        print("\n📋 EXTRATO BANCÁRIO")
        print("=" * 35)
        
        historico = conta.historico.transacoes
        if not historico:
            print("Nenhuma transação foi realizada ainda.")
        else:
            print("Histórico de transações:")
            print("-" * 35)
            for i, transacao in enumerate(historico, 1):
                tipo = transacao['tipo']
                valor = transacao['valor']
                data = transacao['data']
                sinal = '+' if tipo == 'Deposito' else '-'
                print(f"{i:2d}. {tipo}: {sinal}R$ {valor:.2f} - {data}")
        
        print("-" * 35)
        print(f"Saldo atual: R$ {conta.saldo:.2f}")
        if isinstance(conta, ContaCorrente):
            print(f"Saques realizados hoje: {conta.saques_realizados}/{conta.limite_saques}")
        print("=" * 35)
    
    def listar_contas(self):
        """Lista todas as contas"""
        print("\n📋 LISTA DE CONTAS")
        print("=" * 50)
        
        if not self._contas:
            print("Nenhuma conta cadastrada.")
        else:
            for conta in self._contas:
                print(conta)
                print("-" * 50)
    
    def executar(self):
        """Executa o sistema bancário"""
        print("=" * 50)
        print("    SISTEMA BANCÁRIO POO")
        print("=" * 50)
        
        while True:
            print("\n" + "=" * 40)
            print("         MENU PRINCIPAL")
            print("=" * 40)
            print("1 - Criar cliente")
            print("2 - Criar conta corrente")
            print("3 - Saque")
            print("4 - Depósito")
            print("5 - Extrato")
            print("6 - Listar contas")
            print("0 - Sair")
            print("=" * 40)
            
            try:
                opcao = int(input("Escolha uma operação: "))
            except ValueError:
                print("❌ Entrada inválida! Digite apenas números.")
                continue
            
            if opcao == 1:
                self.criar_cliente()
            elif opcao == 2:
                self.criar_conta_corrente()
            elif opcao == 3:
                self.realizar_saque()
            elif opcao == 4:
                self.realizar_deposito()
            elif opcao == 5:
                self.exibir_extrato()
            elif opcao == 6:
                self.listar_contas()
            elif opcao == 0:
                print("\n👋 Saindo do sistema bancário...")
                print("Obrigado por usar nossos serviços!")
                print("Até logo!")
                break
            else:
                print("❌ Operação inválida! Escolha uma opção válida do menu.")
            
            input("\nPressione Enter para continuar...")


# Execução do programa
if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema.executar()