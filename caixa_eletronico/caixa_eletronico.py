from conta_bancaria.conta import ContaBancaria

class CaixaEletronico:
    MENU = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => 
    """

    def __init__(self):
        self.conta = ContaBancaria()

    def iniciar(self):
        while True:
            opcao = input(self.MENU).lower()

            if opcao == "d":
                self.realizar_deposito()
            elif opcao == "s":
                self.realizar_saque()
            elif opcao == "e":
                self.conta.mostrar_extrato()
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