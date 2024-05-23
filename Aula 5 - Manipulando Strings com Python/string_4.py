# String múltiplas linhas

nome = "Jonatas"

mensagem = f"""Olá meu nome é {nome},
Eu estou aprendendo Python.
"""

print(mensagem)

mensagem2 = mensagem = f'''
  Olá meu nome é {nome},
Eu estou aprendendo Python.
    Essa mensagem te diferentes recuos.
'''

print(mensagem2)

print("""
      =========== MENU ===========
      
      1 - Depositar
      2 - Sacar
      0 - Sair
      
      ============================
      
            Obrigado por usar nosso sistema!!!!
      
"""
)