class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor de depósito inválido")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

    def get_saldo(self):
        return self.__saldo

    def extrato(self):
        print(f"Titular: {self.__titular}")
        print(f"Saldo: R$ {self.__saldo:.2f}")


# Teste
conta = ContaBancaria("João")

conta.depositar(1000)
conta.sacar(300)
conta.sacar(800)

conta.extrato()
print("Saldo atual:", conta.get_saldo())