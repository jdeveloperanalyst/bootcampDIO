# Maiúsculas, minúsculas e a primeira sempre maiúscula e o resto minúscula
nome = "Jonatas"

print(nome.upper()) # maiúscula
print(nome.lower()) # minúscula
print(nome.title()) # primeira maiúscula e o resto minúscula


#removendo espaços em branco
texto = "  Olá mundo    "

print(texto + ".") #sem remover nada
print(texto.strip() + ".") # removendo espaços da esquerda e direita
print(texto.rstrip() + ".") # removendo espaços da direita
print(texto.lstrip() + ".") # removendo espaços da esquerda

# Junções e centralizações
menu = "Python"

print(menu)
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(20, "#"))
print("P-y-t-h-o-n")
print("-".join(menu))