class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo     = saldo
        self._numero    = numero
        self._agencia   = agencia
        self._cliente   = cliente #instanciar objeto da classe Cliente
        self._historico = historico
        
    
    def saldo(self):
        return self._saldo
    
    
    def nova_conta(self):
        pass
    
    
    def sacar(self, valor):
        pass
    
    
    def depositar(self, valor):
        pass
        