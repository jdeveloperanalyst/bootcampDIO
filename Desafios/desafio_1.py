# Criando um sistema Bancário com Python v.1

menu = '''
    [1] - Deposito
    [2] - Sacar
    [3] - Extrato
    [0] - Sair
    
    =>
'''
saldo = 0.0
deposito = 0.0

while True:
    print(menu)
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
            
        saldo = deposito
        
        print()
        print(f'Você depositou R${deposito:.2f}, seu saldo atual é R${saldo:.2f}')
    elif opcao == 2:
        print('Saque')
    elif opcao == 3:
        print('Extrato')
    else:
        if opcao == 0:
            print('Saiu do app do banco')
            break