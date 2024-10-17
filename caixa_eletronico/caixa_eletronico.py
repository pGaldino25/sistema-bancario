from conta_bancaria.conta import ContaBancaria

class CaixaEletronico:
    AGENCIA = "0001"
    MENU = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar conta
    [q] Sair

    => 
    """

    def __init__(self):
        self.conta = ContaBancaria()
        self.contas = []
        self.usuarios = []

    def iniciar(self):
        while True:
            opcao = input(self.MENU).lower()

            if opcao == "d":
                self.realizar_deposito()
            elif opcao == "s":
                self.realizar_saque()
            elif opcao == "e":
                self.conta.mostrar_extrato()
            elif opcao == "nu":
                self.conta.criar_usuario(self.usuarios)
            elif opcao == "nc":
                numero_conta = len(self.contas) + 1
                conta = self.conta.criar_conta(self.AGENCIA, numero_conta, self.usuarios)
                if conta:
                    self.contas.append(conta)
            elif opcao == "lc":
                self.conta.listar_contas(self.contas)
            elif opcao == "q":
                print("Saindo...")
                break
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

    def realizar_deposito(self):
        try:
            valor = float(input("Informe o valor do depósito: "))
            self.conta.depositar(valor)
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")

    def realizar_saque(self):
        try:
            valor = float(input("Informe o valor do saque: "))
            self.conta.sacar(valor)
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")