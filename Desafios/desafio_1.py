# Criando um sistema Bancário com Python v.1

menu = '''
########MENU########
    
[1] - Deposito
[2] - Sacar
[3] - Extrato
[0] - Sair

=>
'''
saldo = 0.0
deposito = 0.0
saque = 0.0
extrato = []
cont = 1
LIMITE = 500.00

while True:
    print(menu.lstrip())
    opcao = float(input('Digite uma opção: '))
    if opcao == 1:
        print('#####DEPOSITO#####')
        print(f'#####Saldo atual##### R$:{saldo:.2f}')
        print()
        
        deposito = float(input('Quanto deseja depositar? -> '))
        while deposito <= 0:
            print()
            print('''
            AVISO -> Não é possível depositar valores negativos!\nTente novamente com valores positivos...
            '''.lstrip())
            deposito = float(input('Quanto deseja depositar? -> '))
            
        saldo += deposito
        extrato.append(f'Deposito: R${deposito:.2f}')
        
        print()
        print(f'Você depositou R${deposito:.2f}, seu saldo atual é R${saldo:.2f}')
    elif opcao == 2:
        print('#####SAQUE#####')
        print(f'#####Saldo atual##### R$:{saldo:.2f}')
        print('''
            #####PLANO ATUAL#####\n-> Permissão de 3 saques diários com LIMITE de R$500,00 reais por saque!
            ''')
        print()
        
        saque = float(input('Quanto deseja Sacar? -> '))
        if saque > saldo:
            print(f'Saldo insuficiente! Não será possível SACAR este valor: R${saque:.2f}')
            print(f'O seu saldo atual é: R${saldo:.2f}')
            print()
            continue
        elif cont <= 3:
            if saque <= LIMITE:
                print(f'#####{cont}º SAQUE#####')
                saldo -= saque
                extrato.append(f'Saque: R${saque:.2f}')
                cont += 1
            else:
                print(f'Não foi possível SACAR o valor de R${saque:.2f}!!!')
                print(f'O LIMITE permitido por saque é de R${LIMITE:.2f}')
                print('Tente novamente!')
        else:
            print('Você excedeu a quantidade de 3 saques diários')
        
    elif opcao == 3:
        print('#####EXTRATO DETALHADO#####')
        print(f'-> Saldo atual R$:{saldo:.2f}')
        print()
        if not extrato:
            print('Não possui nenhuma movimentação até o momento!')
        else:
            print('#####TRANSAÇÕES#####')
            for transacao in extrato:
                print(f'-> {transacao}')
        print() 
        print('#####FIM DO EXTRATO#####')    
    else:
        if opcao == 0:
            print('''Muito Obrigado por utilizar os nossos serviços\nO Banco Jonovski Bank Agradece''')
            break