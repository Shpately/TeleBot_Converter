import requests
import telebot

from config import TOKEN, URL
from extensions import Converter, APIException

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
def values(message):
    text = "Список доступных валют: рубль, доллар, евро"
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def convert(message):
    words = message.text.split(' ')
    if len(words) > 3 or len(words) < 2:
        raise APIException("Введите корректное число параметров")
    if base == quote:
        raise APIException("Нельзя конвертировать одну и ту же валюту")
        
    base, quote, amount = words
    price = Converter.get_price(base, quote, amount)
    text = f"Цена {amount} {base} в {quote}: {price}"
    bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
