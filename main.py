import requests
import telebot

from config import TOKEN, URL
from extensions import Converter, APIException

bot = telebot.TeleBot(TOKEN)

# https://apilayer.com/marketplace/order_complete?id=223&txn=free
# https://habr.com/ru/articles/537784/

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

    base, quote, amount = words
    if base == quote:
        raise APIException("Нельзя конвертировать одну и ту же валюту")
    
    try:
        base_true = base
    except KeyError:
        raise APIException("Валюта введена неправильно")
        
    try:
        quote_true = quote
    except KeyError:
        raise APIException("Валюта введена неправильно")
    
    try:
        amount_true = amount
    except KeyError:
        raise APIException("Количество введено неправильно")
        
    price = Converter.get_price(base_true, quote_true, amount_true)
    text = f"Цена {amount_true} {base_true} в {quote_true}: {price}"
    bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
