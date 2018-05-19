import time
import telepot
#import treinabot

from telepot.loop import MessageLoop
from treinabot import add_frase_especifica, add_frase, add_cmd
#from treinabot import *


token = '486176495:AAE98lRmK3LaW7wc2q8nehVYVXqMU9l9peE'
bot = telepot.Bot(token)
frases = {
    'bom': 'Pq bom?\nO que tem de bom?',
    'ruim': 'WOW, pq esse negativismo cara?',
    'zueira': 'Você acha que é zueiro? Não me conheço'
}
comandos = {
    'me_surpreenda': 'HAUSHdUAHDUHDUSAHDUHASUD, me obrigue!'
}

def processa_mensagem(mensagem):
    if 'bom' in mensagem:
        resposta = frases['bom']
    elif 'ruim' in mensagem:
        resposta = frases['ruim']
    elif 'zueira' in mensagem:
        resposta = frases['zueira']
    return resposta


def processa_comando(mensagem):
    if 'me_surpreenda' in mensagem:
        resposta = comandos['me_surpreenda']
    return resposta
        

def manipula_mensagem(objeto_mensagem):
    print('\nUpdate recebido : {}'.format(objeto_mensagem))
    mensagem = objeto_mensagem['text'].lower()
    id_chat = objeto_mensagem['chat']['id']
    print('Mensagem enviada pelo usuário --> {}'.format(mensagem))
    if '/' in mensagem:
        resposta = processa_comando(mensagem)
    else:
        resposta = processa_mensagem(mensagem)
    bot.sendMessage(id_chat, resposta)


MessageLoop(bot, manipula_mensagem).run_as_thread()

while True:
    time.sleep(1)