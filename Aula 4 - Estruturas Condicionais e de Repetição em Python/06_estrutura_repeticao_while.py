# Comando while
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n:"))
    if opcao == 1:
        print("Sacando... ")
    elif opcao == 2:
        print("Exibindo o extrato... ")
else:
    """_Observação_
    -> Não é tão comum do nosso cotidiano utilizar o else após o while,
    -> mas, é apenas para mostrar que é possível.
    """
    print("Obrigado por usar nosso sistema bancário, até logo!")