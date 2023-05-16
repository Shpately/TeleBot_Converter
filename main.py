import telebot

from config import TOKEN, URL
from extensions import Converter, APIException, keys

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    text = "Здравствуйте! С помощью этого бота вы " \
           "можете узнать курс валют. Чтобы узнать список " \
           "доступных валют, введите команду /values.\n" \
           "Чтобы узнать курс валют отправите сообщение боту в виде " \
           "<имя валюты, цену которой хотите узнать> " \
           "<имя валюты, в которой надо узнать цену первой валюты> " \
           "<количество первой валюты>"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message):
    text = "Список доступных валют: рубль, доллар, евро"
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def convert(message):
    words = message.text.split(' ')
    try:
        if len(words) != 3:
            bot.send_message(message.chat.id, 'Введите корректное число параметров')
        else:
            base, quote, amount = words
            price = Converter.get_price(base, quote, amount, bot, message)
            text = f"Цена {amount} {base} в {quote}: {price}"
            bot.send_message(message.chat.id, text)
    except APIException:
        bot.send_message(message.chat.id, 'Проверьте введенные данные')


if __name__ == '__main__':
    bot.polling(none_stop=True)
