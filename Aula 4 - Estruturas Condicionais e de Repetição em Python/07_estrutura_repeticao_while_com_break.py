# Comando while
opcao = -1

while True:
    numero = int(input("Informe um número: "))
    if numero == 10:
        break
    
    print(numero)
    
# É possível usar o break no for também
# O break vai parar a execução
for numero in range(100):
    if numero == 12:
        break
    
    print(numero, end=" ")

# Além do break existe a variação continue
# O continue vai pular a execução
for numero in range(100):
    if numero == 12:
        continue
    
    print(numero, end=" ")
