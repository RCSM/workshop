from getpass import getpass

"""
Validador de login
"""

senha_correta = 42
usuario_correto = 'estudante@workshop.com'

usuario = input('Usuario...: ')
senha = getpass('Senha.....: ')
while usuario != usuario_correto or senha != senha_correta:
    print('Login invalido!')
    usuario = input('Usuario...: ')
    senha = getpass('Senha.....: ')
print('Acesso permitido')