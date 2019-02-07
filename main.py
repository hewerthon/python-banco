from clientes import Clientes
from contas import Contas

cliente1 = Clientes('Hewerthon', '321.456.789-54', 28)

conta1 = Contas(cliente1, 100, 50)
print(conta1.cliente)
print('Saldo: ', conta1.consultar_salto())
print('Limite: ', conta1.limite)
conta1.sacar(130)
print('Saldo: ', conta1.consultar_salto())
conta1.depositar(50)
print('Saldo: ', conta1.consultar_salto())
conta1.sacar(130)
print('Saldo: ', conta1.consultar_salto())



