# 🏦 Sistema Bancário Simples

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)

*Um sistema bancário simples e intuitivo desenvolvido em Python*

[🚀 Começar](#-como-executar) • [📋 Funcionalidades](#-funcionalidades) • [🛠️ Tecnologias](#️-tecnologias) • [📖 Documentação](#-documentação)

</div>

---

## 📖 Sobre o Projeto

Este projeto implementa um sistema bancário básico que simula operações fundamentais de uma conta corrente. Desenvolvido com foco na simplicidade e experiência do usuário, oferece uma interface de linha de comando intuitiva para gerenciar transações bancárias.

### 🎯 Objetivo

Criar uma aplicação que demonstre conceitos fundamentais de programação como:
- Estruturas de controle
- Validação de dados
- Manipulação de listas
- Interface com usuário
- Boas práticas de código

---

## ✨ Funcionalidades

### 💰 **Operações Bancárias**
- **Saque**: Retirada de valores com validações de limite e saldo
- **Depósito**: Adição de valores à conta
- **Extrato**: Visualização completa do histórico de transações

### 🔒 **Segurança e Validações**
- ✅ Validação de valores negativos
- ✅ Controle de limite por saque (R$ 500,00)
- ✅ Limite de saques diários (3 operações)
- ✅ Verificação de saldo suficiente
- ✅ Tratamento de entradas inválidas

### 🎨 **Interface**
- 📱 Menu interativo e intuitivo
- 🎯 Feedback visual com emojis
- 📊 Histórico detalhado de operações
- ⚡ Navegação fluida entre operações

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado
- Terminal/Prompt de comando

### Instalação e Execução

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/sistema-bancario.git

# Navegue até o diretório
cd sistema-bancario

# Execute o programa
python sistema_bancario.py
```

### 🎮 Como Usar

1. **Inicie o programa** - Execute o script Python
2. **Escolha uma operação** - Digite o número correspondente no menu
3. **Siga as instruções** - O sistema guiará você através de cada operação
4. **Visualize resultados** - Confirme suas transações no extrato

---

## 🖥️ Interface do Sistema

```
==================================================
    SISTEMA BANCÁRIO SIMPLES
==================================================
Saldo inicial: R$ 1000.00
Limite por saque: R$ 500.00
Saques diários disponíveis: 3
==================================================

==============================
   MENU DE OPERAÇÕES
==============================
1 - Saque
2 - Depósito
3 - Extrato
0 - Sair
==============================
```

---

## 📊 Exemplos de Uso

### 💸 Realizando um Saque
```
💰 OPERAÇÃO DE SAQUE
-------------------------
Digite o valor do saque: R$ 150.00
✅ Saque realizado com sucesso!
Valor sacado: R$ 150.00
Saldo atual: R$ 850.00
Saques restantes hoje: 2
```

### 💳 Fazendo um Depósito
```
💳 OPERAÇÃO DE DEPÓSITO
--------------------------
Digite o valor do depósito: R$ 300.00
✅ Depósito realizado com sucesso!
Valor depositado: R$ 300.00
Saldo atual: R$ 1150.00
```

### 📋 Consultando o Extrato
```
📋 EXTRATO BANCÁRIO
===================================
Histórico de operações:
-----------------------------------
 1. Saque: -R$ 150.00
 2. Depósito: +R$ 300.00
-----------------------------------
Saldo atual: R$ 1150.00
Saques realizados hoje: 1/3
===================================
```

---

## 🛠️ Tecnologias

<div align="center">

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | 3.8+ | Linguagem principal |
| ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) | Latest | Controle de versão |

</div>

---

## 📁 Estrutura do Projeto

```
sistema-bancario/
│
├── 📄 sistema_bancario.py    # Código principal do sistema
├── 📄 README.md              # Documentação do projeto
├── 📄 LICENSE                # Licença MIT
└── 📁 docs/                  # Documentação adicional
    └── 📄 manual_usuario.md  # Manual detalhado
```

---

## 🔧 Configurações Padrão

| Parâmetro | Valor | Descrição |
|-----------|-------|-----------|
| Saldo inicial | R$ 1.000,00 | Valor inicial da conta |
| Limite por saque | R$ 500,00 | Valor máximo por operação |
| Saques diários | 3 | Quantidade máxima de saques |

---

## 🚦 Status do Projeto

- [x] ✅ Operações básicas (Saque, Depósito, Extrato)
- [x] ✅ Validações de segurança
- [x] ✅ Interface de usuário
- [x] ✅ Tratamento de erros
- [x] ✅ Documentação completa
- [ ] 🔄 Persistência de dados
- [ ] 🔄 Sistema de múltiplas contas
- [ ] 🔄 Interface gráfica

---

## 🤝 Como Contribuir

Contribuições são sempre bem-vindas! Para contribuir:

1. **Fork** o projeto
2. **Crie** uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra** um Pull Request

### 💡 Ideias para Contribuição
- Adicionar novos tipos de conta
- Implementar sistema de transferências
- Criar interface gráfica
- Adicionar testes automatizados
- Melhorar a documentação

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

**Akbar** 
- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- Email: seu.email@exemplo.com

---

## 🙏 Agradecimentos

- Inspirado nos desafios de programação do bootcamp Santander
- Comunidade Python pela documentação e suporte
- Todos que contribuíram com feedback e sugestões

---

<div align="center">

### ⭐ Se este projeto te ajudou, considere dar uma estrela!

**Desenvolvido com ❤️ por [Akbar](https://github.com/seu-usuario)**

</div>