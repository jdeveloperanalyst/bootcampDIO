# Estrutura de repetição for

# for utilizando um iterável com in, e for com else
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    """_Observação_
    -> Não é tão comum do nosso cotidiano utilizar o else após o for,
    -> mas, é apenas para mostrar que é possível.
    """
    print() #adiciona uma quebra de linha
    print("Executa no final do laço")
    
print("--------------------------------------")

# for com a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")
