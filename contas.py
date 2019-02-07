class Contas:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite

    def sacar(self, saque):
        if self.saldo - saque < self.limite:
            print('Erro: Limite insuficiente! Valor do saque: ' + str(saque))
        else:
            self.saldo -= saque
            print('Foi sacado: ' + str(saque))

    def depositar(self, deposito):
        if deposito > 0:
            self.saldo += deposito
            print('Foi depositado: ' + str(deposito))

    def consultar_salto(self):
        return self.saldo
