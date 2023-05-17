import requests
import json

keys = {'доллар': 'USD',
        'евро': 'EUR',
        'рубль': 'RUB'}

payload = {}
headers = {
    "apikey": "ipT969LyS8V3ywjZGmnsUgDEvEPMIgwU"
}


class APIException(Exception):
    pass


class Converter:
    def __init__(self):
        pass

    @staticmethod
    def get_price(base, quote, amount, bot, message):
        base_true, quote_true = None, None
        
        try:
            base_true = keys[base]
        except KeyError:
            bot.send_message(message.chat.id, 'Валюта введена неправильно')
            # raise APIException("Валюта введена неправильно")

        try:
            quote_true = keys[quote]
        except KeyError:
            bot.send_message(message.chat.id, 'Валюта введена неправильно')
            # raise APIException("Валюта введена неправильно")

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={quote_true}&from={base_true}&amount={amount}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            if base_true == quote_true:
                raise APIException("Нельзя конвертировать одну и ту же валюту")

            result = json.loads(response.content)['result']
            return result
        else:
            bot.send_message(message.chat.id, f"Взаимодействие с API невозможно: {response.status_code}")
            # raise ConnectionError(f"Взаимодействие с API невозможно: {response.status_code}")
