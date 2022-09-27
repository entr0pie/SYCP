from email import message
import json

import telebot

token_file = open("credentials/token.json", "r")
token_file = token_file.read()
dict = json.loads(token_file)

TOKEN = dict["TOKEN"]

bot = telebot.TeleBot(TOKEN)

### COMANDOS PRECISAM VIR ANTES ###

@bot.message_handler(commands=["start"])
def recepcao(mensagem):
    greet =  "BEM VINDO A PIZZARIA DO RAUL\n"
    greet += "1. FAZER PEDIDO\n"
    greet += "2. SUGESTÃO?\n"
    greet += "3. SAIR"
    bot.send_message(mensagem.chat.id, greet)

@bot.message_handler()
def handler(mensagem):
    text = mensagem.text.strip().lower()
    
    if "pedido" in text:
        fazer_pedido(mensagem)

    if "sugestao" in text:
        fazer_sugestao(mensagem)

    if "sair" in text:
        sair(mensagem)

def fazer_pedido(mensagem):
    cardapio = "1. FRANGO COM CATUPIRY\n"
    cardapio += "2. QUATRO QUEIJOS\n"
    cardapio += "3. BOLONHESA\n"
    bot.send_message(mensagem.chat.id, cardapio)

def fazer_sugestao(mensagem):
    sug = "DIGITE A SUA SUGESTÃO"
    bot.send_message(mensagem.chat.id, sug)

def sair(mensagem):
    goodbye = "TCHAU!"
    bot.send_message(mensagem.chat.id, goodbye)


bot.polling()