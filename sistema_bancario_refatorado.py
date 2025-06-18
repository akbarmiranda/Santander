# Sistema Bancário Refatorado com Funções
# Operações: Saque, Depósito, Extrato, Criar Usuário, Criar Conta Corrente

import re
from datetime import datetime

# Listas para armazenar dados
usuarios = []
contas = []
numero_conta_sequencial = 1

def validar_cpf(cpf):
    """Valida se o CPF tem formato correto (apenas números)"""
    return cpf.isdigit() and len(cpf) == 11

def buscar_usuario_por_cpf(cpf):
    """Busca um usuário na lista pelo CPF"""
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def criar_usuario():
    """Função para criar um novo usuário"""
    print("\n👤 CRIAR NOVO USUÁRIO")
    print("-" * 30)
    
    # Coleta dados do usuário
    nome = input("Digite o nome completo: ").strip()
    if not nome:
        print("❌ Nome não pode estar vazio!")
        return
    
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ").strip()
    if not re.match(r'\d{2}/\d{2}/\d{4}', data_nascimento):
        print("❌ Formato de data inválido! Use DD/MM/AAAA")
        return
    
    cpf = input("Digite o CPF (apenas números): ").strip()
    if not validar_cpf(cpf):
        print("❌ CPF inválido! Digite apenas 11 números.")
        return
    
    # Verifica se CPF já existe
    if buscar_usuario_por_cpf(cpf):
        print("❌ Já existe um usuário cadastrado com este CPF!")
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
    
    # Cria o usuário
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    
    usuarios.append(usuario)
    print("✅ Usuário criado com sucesso!")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")

def criar_conta_corrente():
    """Função para criar uma nova conta corrente"""
    global numero_conta_sequencial
    
    print("\n🏦 CRIAR CONTA CORRENTE")
    print("-" * 30)
    
    if not usuarios:
        print("❌ Nenhum usuário cadastrado! Crie um usuário primeiro.")
        return
    
    cpf = input("Digite o CPF do usuário: ").strip()
    if not validar_cpf(cpf):
        print("❌ CPF inválido! Digite apenas 11 números.")
        return
    
    # Busca o usuário
    usuario = buscar_usuario_por_cpf(cpf)
    if not usuario:
        print("❌ Usuário não encontrado!")
        return
    
    # Verifica se o usuário já possui conta
    for conta in contas:
        if conta['usuario']['cpf'] == cpf:
            print("❌ Este usuário já possui uma conta corrente!")
            return
    
    # Cria a conta
    conta = {
        'agencia': '0001',
        'numero_conta': numero_conta_sequencial,
        'usuario': usuario,
        'saldo': 0.0,
        'limite_saque': 500.0,
        'saques_realizados': 0,
        'limite_saques_diarios': 3,
        'historico_operacoes': []
    }
    
    contas.append(conta)
    numero_conta_sequencial += 1
    
    print("✅ Conta corrente criada com sucesso!")
    print(f"Agência: {conta['agencia']}")
    print(f"Conta: {conta['numero_conta']}")
    print(f"Titular: {usuario['nome']}")

def selecionar_conta():
    """Função para selecionar uma conta para operações"""
    if not contas:
        print("❌ Nenhuma conta cadastrada!")
        return None
    
    print("\n📋 CONTAS DISPONÍVEIS:")
    print("-" * 40)
    for i, conta in enumerate(contas):
        print(f"{i+1}. Ag: {conta['agencia']} - Conta: {conta['numero_conta']} - {conta['usuario']['nome']}")
    
    try:
        escolha = int(input("\nSelecione o número da conta: ")) - 1
        if 0 <= escolha < len(contas):
            return contas[escolha]
        else:
            print("❌ Conta inválida!")
            return None
    except ValueError:
        print("❌ Entrada inválida!")
        return None

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Função para realizar saque (keyword only)"""
    # Verifica se ainda tem saques disponíveis
    if numero_saques >= limite_saques:
        print("❌ Limite de saques diários atingido!")
        print(f"Você já realizou {numero_saques} saques hoje.")
        return saldo, extrato
    
    # Validações do saque
    if valor <= 0:
        print("❌ Valor inválido! O valor deve ser positivo.")
    elif valor > limite:
        print(f"❌ Valor excede o limite de saque de R$ {limite:.2f}")
    elif valor > saldo:
        print("❌ Saldo insuficiente para realizar o saque.")
        print(f"Seu saldo atual é de R$ {saldo:.2f}")
    else:
        # Realiza o saque
        saldo -= valor
        extrato.append(f"Saque: -R$ {valor:.2f}")
        
        print("✅ Saque realizado com sucesso!")
        print(f"Valor sacado: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print(f"Saques restantes hoje: {limite_saques - numero_saques - 1}")
        
        return saldo, extrato
    
    return saldo, extrato

def deposito(saldo, valor, extrato, /):
    """Função para realizar depósito (positional only)"""
    # Validações do depósito
    if valor <= 0:
        print("❌ Valor inválido! O valor deve ser positivo.")
    else:
        # Realiza o depósito
        saldo += valor
        extrato.append(f"Depósito: +R$ {valor:.2f}")
        
        print("✅ Depósito realizado com sucesso!")
        print(f"Valor depositado: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    """Função para exibir extrato (positional only e keyword only)"""
    print("\n📋 EXTRATO BANCÁRIO")
    print("=" * 35)
    
    if not extrato:
        print("Nenhuma operação foi realizada ainda.")
    else:
        print("Histórico de operações:")
        print("-" * 35)
        for i, operacao in enumerate(extrato, 1):
            print(f"{i:2d}. {operacao}")
    
    print("-" * 35)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=" * 35)

def listar_contas():
    """Função para listar todas as contas"""
    print("\n📋 LISTA DE CONTAS")
    print("=" * 50)
    
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            usuario = conta['usuario']
            print(f"Agência: {conta['agencia']}")
            print(f"C/C: {conta['numero_conta']}")
            print(f"Titular: {usuario['nome']}")
            print(f"Saldo: R$ {conta['saldo']:.2f}")
            print("-" * 50)

def main():
    """Função principal do sistema"""
    print("=" * 50)
    print("    SISTEMA BANCÁRIO REFATORADO")
    print("=" * 50)
    
    while True:
        # Menu principal
        print("\n" + "=" * 40)
        print("         MENU PRINCIPAL")
        print("=" * 40)
        print("1 - Criar usuário")
        print("2 - Criar conta corrente")
        print("3 - Saque")
        print("4 - Depósito")
        print("5 - Extrato")
        print("6 - Listar contas")
        print("0 - Sair")
        print("=" * 40)
        
        try:
            operacao = int(input("Escolha uma operação: "))
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números.")
            continue
        
        if operacao == 1:
            criar_usuario()
            
        elif operacao == 2:
            criar_conta_corrente()
            
        elif operacao == 3:
            print("\n💰 OPERAÇÃO DE SAQUE")
            print("-" * 25)
            
            conta = selecionar_conta()
            if not conta:
                continue
            
            try:
                valor_saque = float(input("Digite o valor do saque: R$ "))
            except ValueError:
                print("❌ Valor inválido! Digite um número válido.")
                continue
            
            # Chama a função saque
            conta['saldo'], conta['historico_operacoes'] = saque(
                saldo=conta['saldo'],
                valor=valor_saque,
                extrato=conta['historico_operacoes'],
                limite=conta['limite_saque'],
                numero_saques=conta['saques_realizados'],
                limite_saques=conta['limite_saques_diarios']
            )
            
            # Atualiza contador se saque foi realizado
            if len(conta['historico_operacoes']) > 0 and "Saque" in conta['historico_operacoes'][-1]:
                if valor_saque > 0 and valor_saque <= conta['limite_saque'] and valor_saque <= (conta['saldo'] + valor_saque):
                    conta['saques_realizados'] += 1
        
        elif operacao == 4:
            print("\n💳 OPERAÇÃO DE DEPÓSITO")
            print("-" * 26)
            
            conta = selecionar_conta()
            if not conta:
                continue
            
            try:
                valor_deposito = float(input("Digite o valor do depósito: R$ "))
            except ValueError:
                print("❌ Valor inválido! Digite um número válido.")
                continue
            
            # Chama a função depósito
            conta['saldo'], conta['historico_operacoes'] = deposito(
                conta['saldo'],
                valor_deposito,
                conta['historico_operacoes']
            )
        
        elif operacao == 5:
            conta = selecionar_conta()
            if not conta:
                continue
            
            # Chama a função extrato
            exibir_extrato(conta['saldo'], extrato=conta['historico_operacoes'])
            print(f"Saques realizados hoje: {conta['saques_realizados']}/{conta['limite_saques_diarios']}")
        
        elif operacao == 6:
            listar_contas()
        
        elif operacao == 0:
            print("\n👋 Saindo do sistema bancário...")
            print("Obrigado por usar nossos serviços!")
            print("Até logo!")
            break
        
        else:
            print("❌ Operação inválida! Escolha uma opção válida do menu.")
        
        # Pausa para o usuário ver o resultado
        input("\nPressione Enter para continuar...")

# Executa o programa principal
if __name__ == "__main__":
    main()