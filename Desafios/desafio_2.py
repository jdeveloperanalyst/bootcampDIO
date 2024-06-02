# Refatorando o sistema Bancário do desafio_1 com Python v.2

def menu_principal():
    menu = f'''\n{'MENU'.center(41, '#')}

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Criar Usuário
[5] - Criar Conta Corrente
[6] - Consultar Usuário
[7] - Listar Usuários
[0] - Sair

=> '''
    return menu


def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato.append(f'{"Deposito".ljust(32, ".")}R${valor:.2f}')
    else:
        print('Operação falhou! O valor informado é inválido.')
    return saldo , extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques
    if excedeu_saldo:
        print('Operação falhou! Você não tem saldo suficiente.')
    elif excedeu_limite:
        print('Operação falhou! O valor do saque excede o limite.')
    elif excedeu_saques:
        print('Operação falhou! Número máximo de saques excedido.')
    elif valor > 0:
        saldo -= valor
        extrato.append(f'{"Saque".ljust(32, ".")}R${valor:.2f}')
        numero_saques += 1
    else:
        print('Operação falhou! O valor informado é inválido.')
    return saldo, extrato, numero_saques


def extrato(saldo,/,*,extrato):
    print('\n================ EXTRATO ================')
    if extrato:
        for transacao in extrato:
            print(transacao)
    else:
        print('Não foram realizadas movimentações.')
    print(f'\n{"Saldo".ljust(32, ".")}R${saldo:.2f}')
    print('=========================================')
    return ''


def criar_usuario(list_users):
    nome = str(input('Nome completo => '))
    data_nascimento = str(input('Data de Nascimento => '))
    cpf = int(input('CPF (sem os pontos/traços) => '))
    for user in list_users:
        if cpf == user['cpf']:
            print('O CPF já existe em nossa base de dados\n')
            print(user)
            return list_users
    endereco = ' - '.join([str(input('Logradouro => ')), str(input('Número => ')), str(input('Bairro => ')), str(input('Cidade/Sigla Estado => '))])
    
    usuario = {'nome': nome, 'data nascimento': data_nascimento, 'cpf': cpf, 'endereço': endereco}
    list_users.append(usuario)
    return list_users


def criar_conta_corrente(list_users, contas):
    if len(list_users) > 0:
        cpf = int(input('Informe o cpf(sem pontos/traços) => '))
        cpf_encontrado = False
        for user in list_users: 
            if cpf == user['cpf']:
                conta = ' | '.join(['agência: 0001', f'conta {len(contas)+1}'])
                contas.append(conta)
                if 'conta(s)' in user:
                    user['conta(s)'].add(conta)
                else:
                    user['conta(s)'] = {conta}
                cpf_encontrado = True
        if not cpf_encontrado:
            print('\nO CPF não existe em nossa base de dados')
            return list_users, contas
    else:
        print('O banco ainda não possui usuários')
    return list_users, contas
        

def consultar_usuario(list_users):
    if len(list_users) > 0:
        cpf = int(input('Informe o cpf(sem pontos/traços) => '))
        cpf_encontrado = False
        for user in list_users:
            if cpf == user['cpf']:
                print('=' * 60)
                for chave, valor in user.items():
                    print(f'{chave}: {valor}')
                print('=' * 60)
                cpf_encontrado = True
        if not cpf_encontrado:
            print('CPF não existe em nossa base de dados!')
    else:
        print('O banco ainda não possui usuários')
        

def listar_usuarios(list_users):
    if len(list_users) > 0:
        for user in list_users:
            print('=' * 60)
            for chave, valor in user.items():
                print(f'{chave}: {valor}')
            print('=' * 60)
    else:
        print('O banco ainda não possui usuários')
        
       
if __name__ == '__main__':
    saldo = 0
    extrato_detalhado = []
    numero_saques = 1
    lista_usuarios = [] 
    contas = []
       
    while True:
        opcao = int(input(menu_principal()))
        if opcao == 1:
            valor = float(input('\nInforme o valor do depósito: '))
            saldo, extrato_detalhado =  depositar(saldo, valor, extrato_detalhado)
        elif opcao == 2:
            valor = float(input('\nInforme o valor do saque: '))
            saldo, extrato_detalhado, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato_detalhado, limite=500, numero_saques=numero_saques, limite_saques=3)
        elif opcao == 3:
            extrato(saldo, extrato=extrato_detalhado)
        elif opcao == 4:
            print('\nCriar Usuário\n')
            lista_usuarios = criar_usuario(lista_usuarios)
        elif opcao == 5:
            print('\nCriar Conta Corrente\n')
            lista_usuarios, contas = criar_conta_corrente(lista_usuarios, contas)
        elif opcao == 6:
            print('\nConsulta de Usuarios\n')
            consultar_usuario(lista_usuarios)
        elif opcao == 7:
            print('\nLista de Usuários\n')
            listar_usuarios(lista_usuarios)
        elif opcao == 0:
            print(f'\nMuito Obrigado por utilizar os nossos serviços.\nVolte Sempre :)\n')
            break
        else:
            print('\nOpção invalida, por favor selecione novamente a operação realizada.')