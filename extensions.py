import requests
import json

keys = {'доллар' : 'USD',
        'евро' : 'EUR',
        'рубль' : 'RUR'}

payload = {}
headers= {
        "apikey": "ipT969LyS8V3ywjZGmnsUgDEvEPMIgwU"
        }
    
    
class Converter:
    def __init__(self):
        pass
   
    @staticmethod
    def get_price(base, quote, amount):
        if base, quote in keys:
                url = f"https://api.apilayer.com/exchangerates_data/convert?to={keys[base]}&from={keys[quote]}&amount={amount}"
                response = requests.request("GET", url, headers=headers, data = payload)

                if response.status_code == 200:
                    result = json.loads[response.content]
                    return result
                    # raise ValueError(f"Invalid response format from API: {data}")
                else:
                    raise ConnectionError(f"Failed to fetch data from API: {response.status_code}")
        else:
            return "Введите корректные данные"
           
