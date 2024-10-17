from datetime import datetime


def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return resultado

    return envelope

class ContaBancaria:
    LIMITE_SAQUES = 3
    LIMITE_SAQUE_VALOR = 500
    AGENCIA = "0001"

    def __init__(self):
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0
        self.usuarios = []
        self.contas = []
    
    
    @log_transacao
    def depositar(self, valor, /):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    @log_transacao
    def sacar(self, valor):
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif valor > self.saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > self.LIMITE_SAQUE_VALOR:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {self.LIMITE_SAQUE_VALOR:.2f}.")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def mostrar_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

    
    def criar_usuario(self, nome):  
        cpf = input("Informe o CPF (somente números): ")
        self.usuario = self.filtrar_usuario(cpf, self.usuarios)
        if self.usuario:
            print("\nJa existe um usuário com este CPF.")
            return
        
        nome = input("Informa o nome completo: ")
        data_nascimento = input("Informa a data de nascimento (DD/MM/AAAA): ")
        endereco = input("Informa o endereço (logradouro, nro - bairro - cidade/uf): ")

        self.usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("\n=== Usuario criado com sucesso! ===")
    

    def filtrar_usuario(self, cpf, usuarios):
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                return usuario
        return None

    
    def criar_conta(self, agencia, numero_conta, usuarios):
        usuario = self.filtrar_usuario(input("Informa o CPF do usuário: "), self.usuarios)
        if usuario:
            print("=== Conta criada com sucesso! ===")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

        print("\n @@@ Usuário não encontrado, fluxo de criação de conta encerrado @@@")

    
    def listar_contas(self, contas):
        for conta in contas:
            print(f"\nAgência: {conta['agencia']}")
            print(f"Conta: {conta['numero_conta']}")
            print(f"Titular: {conta['usuario']['nome']}")