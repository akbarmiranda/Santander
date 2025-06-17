# Sistema Bancário Simples
# Operações: Saque, Depósito, Extrato e Sair

def main():
    # Variáveis iniciais
    saldo = 1000.0
    limite_saque = 500.0
    saques_realizados = 0
    limite_saques_diarios = 3
    historico_operacoes = []
    
    print("=" * 50)
    print("    SISTEMA BANCÁRIO SIMPLES")
    print("=" * 50)
    print(f"Saldo inicial: R$ {saldo:.2f}")
    print(f"Limite por saque: R$ {limite_saque:.2f}")
    print(f"Saques diários disponíveis: {limite_saques_diarios}")
    print("=" * 50)
    
    while True:
        # Menu de operações
        print("\n" + "=" * 30)
        print("   MENU DE OPERAÇÕES")
        print("=" * 30)
        print("1 - Saque")
        print("2 - Depósito") 
        print("3 - Extrato")
        print("0 - Sair")
        print("=" * 30)
        
        try:
            operacao = int(input("Escolha uma operação: "))
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números.")
            continue
            
        # Operação de Saque
        if operacao == 1:
            print("\n💰 OPERAÇÃO DE SAQUE")
            print("-" * 25)
            
            # Verifica se ainda tem saques disponíveis
            if saques_realizados >= limite_saques_diarios:
                print("❌ Limite de saques diários atingido!")
                print(f"Você já realizou {saques_realizados} saques hoje.")
                continue
                
            try:
                valor_saque = float(input("Digite o valor do saque: R$ "))
            except ValueError:
                print("❌ Valor inválido! Digite um número válido.")
                continue
                
            # Validações do saque
            if valor_saque <= 0:
                print("❌ Valor inválido! O valor deve ser positivo.")
            elif valor_saque > limite_saque:
                print(f"❌ Valor excede o limite de saque de R$ {limite_saque:.2f}")
            elif valor_saque > saldo:
                print("❌ Saldo insuficiente para realizar o saque.")
                print(f"Seu saldo atual é de R$ {saldo:.2f}")
            else:
                # Realiza o saque
                saldo -= valor_saque
                saques_realizados += 1
                historico_operacoes.append(f"Saque: -R$ {valor_saque:.2f}")
                
                print("✅ Saque realizado com sucesso!")
                print(f"Valor sacado: R$ {valor_saque:.2f}")
                print(f"Saldo atual: R$ {saldo:.2f}")
                print(f"Saques restantes hoje: {limite_saques_diarios - saques_realizados}")
        
        # Operação de Depósito        
        elif operacao == 2:
            print("\n💳 OPERAÇÃO DE DEPÓSITO")
            print("-" * 26)
            
            try:
                valor_deposito = float(input("Digite o valor do depósito: R$ "))
            except ValueError:
                print("❌ Valor inválido! Digite um número válido.")
                continue
                
            # Validações do depósito
            if valor_deposito <= 0:
                print("❌ Valor inválido! O valor deve ser positivo.")
            else:
                # Realiza o depósito
                saldo += valor_deposito
                historico_operacoes.append(f"Depósito: +R$ {valor_deposito:.2f}")
                
                print("✅ Depósito realizado com sucesso!")
                print(f"Valor depositado: R$ {valor_deposito:.2f}")
                print(f"Saldo atual: R$ {saldo:.2f}")
        
        # Operação de Extrato
        elif operacao == 3:
            print("\n📋 EXTRATO BANCÁRIO")
            print("=" * 35)
            
            if not historico_operacoes:
                print("Nenhuma operação foi realizada ainda.")
            else:
                print("Histórico de operações:")
                print("-" * 35)
                for i, operacao_hist in enumerate(historico_operacoes, 1):
                    print(f"{i:2d}. {operacao_hist}")
                    
            print("-" * 35)
            print(f"Saldo atual: R$ {saldo:.2f}")
            print(f"Saques realizados hoje: {saques_realizados}/{limite_saques_diarios}")
            print("=" * 35)
        
        # Sair do sistema
        elif operacao == 0:
            print("\n👋 Saindo do sistema bancário...")
            print("Obrigado por usar nossos serviços!")
            print("Até logo!")
            break
            
        # Operação inválida
        else:
            print("❌ Operação inválida! Escolha uma opção válida do menu.")
            
        # Pausa para o usuário ver o resultado
        input("\nPressione Enter para continuar...")

# Executa o programa principal
if __name__ == "__main__":
    main()