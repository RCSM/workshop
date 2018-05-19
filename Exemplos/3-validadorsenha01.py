senha_correta = 42
senha = int(input('Digite a senha :'))
while senha != senha_correta:
    print('Senha incorreta!')
    senha = int(input('\nDigite a senha novamente :'))
print('Acesso permitido')