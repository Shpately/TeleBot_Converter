import requests
import telebot

from config import TOKEN, URL

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    text = "Здравствуйте! С помощью этого бота вы " \
           "можете узнать курс валют. Чтобы узнать список " \
           "доступных валют, введите команду /values.\n" \
           "Чтобы узнать курс валют отправите сообщение боту в виде " \
           "<имя валюты, цену которой он хочет узнать> " \
           "<имя валюты, в которой надо узнать цену первой валюты> " \
           "<количество первой валюты>"
    bot.send_message(message.chat.id, text)
    # bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def start(message):
    text = "Список доступных валют: рубль, доллар, евро"
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def start(message):
    text = "УУУ"
    bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    # init_db()
    bot.polling(none_stop=True)
