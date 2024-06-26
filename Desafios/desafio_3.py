from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime
import textwrap


class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f'''\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        '''
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1
            
            
class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            }
        )
    
    
    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao
    
    
    def transacoes_do_dia(self):
        data_atual = datetime.now().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(transacao['data'], '%d-%m-%Y %H:%M:%S').date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes    

class Conta:
    def __init__(self, numero, cliente):
        self._saldo     = 0
        self._numero    = numero
        self._agencia   = '0001'
        self._cliente   = cliente
        self._historico = Historico()
        
    
    def saldo(self):
        return self._saldo
    
    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    
    @property
    def saldo(self):
        return self._saldo
    
    
    @property
    def numero(self):
        return self._numero
    
    
    @property
    def agencia(self):
        return self._agencia
    
    
    @property
    def cliente(self):
        return self._cliente
    
    
    @property
    def historico(self):
        return self._historico
    
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print('\n@@@ Operação falhou! Você não tem saldo suficiente. @@@')

        elif valor > 0:
            self._saldo -= valor
            print('\n=== Saque realizado com sucesso! ===')
            return True
        
        else:
            print('\n@@@ Operação falhou! O valor informado é inválido. @@@')

        return False
    

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('\n=== Depósito realizado com sucesso! ===')
        else:
            print('\n@@@ Operação falhou! O valor informado é inválido. @@@')
            return False
        
        return True
    
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        
    
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__])
        
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques
        
        if excedeu_limite:
            print('\n@@@ Operação falhou! O valor do saque excede o limite. @@@')

        elif excedeu_saques:
            print('\n@@@ Operação falhou! Número máximo de saques excedido. @@@')

        else:
            return super().sacar(valor)
        
        return False
    
    
    def __str__(self):
        return f'''\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        '''
        
        
class Cliente:
    def __init__(self, endereco):
        self.endereco    = endereco
        self.contas      = []
        self._indice_conta = 0
    
    
    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print('\n@@@ Você excedeu o número de transações permitidas para hoje! @@@')
            return
        
        transacao.registrar(conta)

    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

    
class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf             = cpf
        self.nome            = nome
        self.data_nascimento = data_nascimento


class Transacao(ABC):
    # Interface
    @property
    @abstractproperty
    def valor(self):
        pass
    
    
    @abstractmethod
    def registrar(self, conta):
        pass
    

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    
    @property
    def valor(self):
        return self._valor
    
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    
    @property
    def valor(self):
        return self._valor
    
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
        

def log_transacao(func):
    def logs(*args, **kwargs):
        if func.__name__ == 'depositar':
            result = func(*args, **kwargs)
            linha = '=' * 10
            print(f'{linha} DEPOSITO {datetime.now().strftime("%d-%m-%Y %H:%M:%S")} {linha}')
        
        elif func.__name__ == 'sacar':
            result = func(*args, **kwargs)
            linha = '=' * 10
            print(f'{linha} SAQUE {datetime.now().strftime("%d-%m-%Y %H:%M:%S")} {linha}')
            
        elif func.__name__ == 'exibir_extrato':
            result = func(*args, **kwargs)
            linha = '=' * 10
            print(f'{linha} EXTRATO {datetime.now().strftime("%d-%m-%Y %H:%M:%S")} {linha}')
        
        elif func.__name__ == 'criar_cliente':
            result = func(*args, **kwargs)
            linha = '=' * 10
            print(f'{linha} NOVO CLIENTE {datetime.now().strftime("%d-%m-%Y %H:%M:%S")} {linha}')
            
        elif func.__name__ == 'criar_conta':
            result = func(*args, **kwargs)
            linha = '=' * 10
            print(f'{linha} NOVA CONTA {datetime.now().strftime("%d-%m-%Y %H:%M:%S")} {linha}')
        return result
    
    return logs


def menu():
    menu = '''\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tNova conta
    [6]\tListar contas
    [0]\tSair
    => '''
    return int(input(textwrap.dedent(menu)))


def menu_extrato():
    menu = '''\n
    ================ EXTRATO ================
    [1]\tExtrato detalhado - (Geral)
    [2]\tExtrato por operação - (Saques ou Depositos)
    => '''
    return int(input(textwrap.dedent(menu)))


def menu_tipo_operacao():
    tipo_operacao = '''\n
    Qual o tipo de operação desejada?
    [1]\tDepositos
    [2]\tSaques
    => '''
    return int(input(textwrap.dedent(tipo_operacao)))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print('\n@@@ Cliente não possui conta! @@@')
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


@log_transacao
def depositar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Cliente não encontrado! @@@')
        return

    valor = float(input('Informe o valor do depósito: '))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def sacar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Cliente não encontrado! @@@')
        return

    valor = float(input('Informe o valor do saque: '))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def exibir_extrato(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Cliente não encontrado! @@@')
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    extrato = ''
    tem_transacao = False
    
    while True:
        opcao = menu_extrato()
        if opcao == 1:
            flag = None
            break
        elif opcao == 2:
            tipo_operacao = menu_tipo_operacao()
            if tipo_operacao == 1:
                flag = 'deposito'
                break
            elif tipo_operacao == 2:
                flag = 'saque'
                break
            else:
                print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")
    for transacao in conta.historico.gerar_relatorio(tipo_transacao=flag):
        tem_transacao = True
        tipo_transacao = transacao['tipo']
        valor_transacao = f'R${transacao["valor"]:.2f}'
        data_transacao = transacao['data']
        num_pontos = 40 - len(tipo_transacao) - len(valor_transacao) - len(data_transacao)
        extrato += f'\n{tipo_transacao}{"." * num_pontos}{valor_transacao}  {data_transacao}'

    if not tem_transacao:
        extrato = "Não foram realizadas movimentações"
        
    saldo_str = f'R${conta.saldo:.2f}'
    num_pontos_saldo = 40 - len('Saldo') - len(saldo_str) - len(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
    saldo = f'\nSaldo{"." * num_pontos_saldo}{saldo_str}  {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}'

    print(extrato)
    print(saldo)
    print('==========================================')


@log_transacao
def criar_cliente(clientes):
    cpf = input('Informe o CPF (somente número): ')
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print('\n@@@ Já existe cliente com esse CPF! @@@')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print('\n=== Cliente criado com sucesso! ===')


@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@')
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print('\n=== Conta criada com sucesso! ===')


def listar_contas(contas):
    for conta in ContasIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


if __name__ == '__main__':
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            depositar(clientes)

        elif opcao == 2:
            sacar(clientes)

        elif opcao == 3:
            exibir_extrato(clientes)

        elif opcao == 4:
            criar_cliente(clientes)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 0:
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")
