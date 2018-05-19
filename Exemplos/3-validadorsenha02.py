# Como daria para fazer esse mesmo código com um else ao invés do continue?

flag = True
senha_correta = 42
senha = int(input('Digite a senha :'))
while flag:
    if senha != senha_correta:
        print('Senha incorreta!')
        senha = int(input('\nDigite a senha novamente :'))
        continue
    flag = False
print('Acesso permitido')