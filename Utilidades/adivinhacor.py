# Como você faria esse jogo mais legal??

from random import randint

cor = randint(0, 2)

if cor == 0:
    cor = 'vermelho'
elif cor == 1:
    cor = 'azul'
elif cor == 2:
    cor = 'verde'

print(' -- Qual é a cor? --\n'
    + '\n,------------------------------------------------------------,'
    + '\n| Uma cor foi aleatoriamente gerada quando esse código rodou |'
    + '\n| As cores possíveis são : vermelho, azul, verde e branco    |'
    + '\n| Quanto antes você acertar mais pontos você consegue        |'
    + "\n'------------------------------------------------------------'")

palpite = input('\n\nDigite seu palpite : ').lower()
for i in range(1000, 0, -100):
    if palpite == cor:
        if i == 1000:
            print('Putz, tu é sortudo hein?? De primeira')
        print('BBBOOOOAAAA! Você ganhou : {}'.format(i))
        break
    elif i == 100:
        print('\n############################'
            + '\n#  É não foi dessa vez :(  #'
            + '\n############################')
    else:
        print('\n===============================================')
        if i == 1000:
            print('\nAh, detalhe : toda vez que você erra a cor que você tem que acertar muda ;)')
    
        cor = randint(0, 2)

        if cor == 0:
            cor = 'vermelho'
        elif cor == 1:
            cor = 'azul'
        elif cor == 2:
            cor = 'verde'

        if i <= 900:
            print('\n - {} pontos'.format(100))
        print('\nValor do palpite : {} pontos :D'.format(i-100))
        palpite = input('\nDigite seu novo palpite : ').lower()