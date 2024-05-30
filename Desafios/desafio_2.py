# Refatorando o sistema Bancário do desafio_1 com Python v.2

def menu_principal():
    menu = '''########MENU########

[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

=> '''
    return menu


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f'{valor:.2f}')
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo , extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques
    if excedeu_saldo:
        print('Operação falhou! Você não tem saldo suficiente.\n')
    elif excedeu_limite:
        print('Operação falhou! O valor do saque excede o limite.\n')
    elif excedeu_saques:
        print('Operação falhou! Número máximo de saques excedido.\n')
    elif valor > 0:
        saldo -= valor
        extrato.append(f'{valor:.2f}')
        numero_saques += 1
    else:
        print('Operação falhou! O valor informado é inválido.\n')
    return saldo, extrato, numero_saques



def extrato():
    return ''


if __name__ == '__main__':
    saldo = 0
    extrato_detalhado = []
    numero_saques = 1
    while True:
        opcao = int(input(menu_principal()))
        if opcao == 1:
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato_detalhado =  depositar(saldo, valor, extrato_detalhado)
            print(f'{saldo}, {extrato_detalhado}\n')
        elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato_detalhado, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato_detalhado, limite=500, numero_saques=numero_saques, limite_saques=3)
            print(f'{saldo}, {extrato_detalhado}\n')
        elif opcao == 0:
            break