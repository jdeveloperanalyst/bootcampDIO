# Criando um sistema Bancário com Python v.1

menu = '''
########MENU########
    
[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

=>
'''
plano = '#####PLANO ATUAL#####\n-> Permissão de 3 saques diários com LIMITE de R$500,00 reais por saque!'
saldo = 0.0
deposito = 0.0
saque = 0.0
extrato = []
numero_saques = 1
LIMITE = 500.00

while True:
    print(menu.lstrip())
    opcao = float(input('Digite uma opção: '))
    print()
    if opcao == 1:
        print('--' * 20)
        print('#####DEPOSITO#####')
        print(f'#####Saldo atual##### R${saldo:.2f}\n')
        
        deposito = float(input('Quanto deseja depositar? -> '))
        if deposito <= 0:
            print('\nAVISO -> Não é possível depositar valores negativos!\n')
            continue
        saldo += deposito
        extrato.append(f'Deposito: R${deposito:.2f}')
        
        print(f'\nVocê depositou R${deposito:.2f}, seu saldo atual é R${saldo:.2f}\n')
        print('--' * 20)
    elif opcao == 2:
        print('--' * 20)
        print('#####SAQUE#####')
        print(plano.lstrip())
        print(f'\n#####Saldo atual##### R${saldo:.2f}\n')
        
        saque = float(input('Quanto deseja Sacar? -> '))
        if saque > saldo:
            print(f'\nSaldo insuficiente! O seu saldo atual é: R${saldo:.2f}.\n')
            print('--' * 20)
            continue
        elif saque < 0:
            print('\nNão é possível SACAR um valor negativo\n')
            print('--' * 20)
        elif numero_saques <= 3:
            if saque <= LIMITE:
                print(f'#####{numero_saques}º SAQUE#####\n')
                saldo -= saque
                extrato.append(f'Saque: R${saque:.2f}')
                numero_saques += 1
                print('--' * 20)
            else:
                print(f'\nNão foi possível SACAR o valor de R${saque:.2f}.')
                print(f'O LIMITE permitido por saque é de R${LIMITE:.2f}.')
                print('Tente novamente..\n')
                print('--' * 20)
        else:
            print('Você excedeu a quantidade de 3 saques diários')
        
    elif opcao == 3:
        print('--' * 20)
        print('#####EXTRATO DETALHADO#####\n')
        if not extrato:
            print('--' * 20) 
            print('Não possui nenhuma movimentação até o momento!')
        else:
            print('#####TRANSAÇÕES#####\n')
            for transacao in extrato:
                print(f'-> {transacao}')

        print(f'\nSaldo atual R${saldo:.2f}')
        print('\n#####FIM DO EXTRATO#####\n') 
        print('--' * 20)   
    elif opcao == 0:
            print('--' * 20) 
            print('''\nMuito Obrigado por utilizar os nossos serviços.\n''')
            break
    else:
        print('\nOpção invalida, por favor selecione novamente a operação realizada.')