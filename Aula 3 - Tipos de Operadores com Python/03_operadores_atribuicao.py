#Operadores de atribuição

saldo = 500    #atribuição simples -> variavel saldo recebe 500 | output: 500
print(saldo)

saldo = 200    #atribuição simples -> variavel saldo recebe 200 | output: 200
print(saldo)

saldo += 10    #atribuição com adição -> variavel saldo recebe 200 mais 10 | output: 210
print(saldo)

saldo -= 5     #atribuição com subtração -> variavel saldo recebe 210 menos  | output: 205
print(saldo)

saldo //= 2    #atribuição com divisão inteira -> variavel saldo recebe 205 dividido por 2 | output: 102
print(saldo)

saldo /= 2      #atribuição com divisão com ponto flutuante -> variavel saldo recebe 102 dividido por 2 | output: 51.0
print(saldo)

saldo *= 10      #atribuição com multiplicação -> variavel saldo recebe 51 multiplicado por 10 | output: 510
print(saldo)

saldo %= 4    #atribuição com resto de divisão -> variavel saldo recebe 510 resto de divisão por 4 | output 2.0
print(saldo)

saldo **= 2     #atribuição com exponenciação -> variavel saldo recebe 2.0 elevado ao quadrado | output: 4.0
print(saldo)
