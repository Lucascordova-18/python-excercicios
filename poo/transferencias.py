class ContaBancaria:
    def __init__(self, name,  saldo):
        self.name = name
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, value):
        self._saldo = value

    def transferir(self, outra_conta, value):
        if value < 0:
            raise ValueError("A transferencia nao pode ser negativa")
        if value > self._saldo:
            raise ValueError ("Voce nao tem esse valor disponivel")
        
        self._saldo -= value
        outra_conta._saldo += value
        
c1 = ContaBancaria("Lucas", 1000)
c2 = ContaBancaria("Mariana", 120)


c1.transferir(c2, 100)
print(c1.saldo)
print(c2.saldo)