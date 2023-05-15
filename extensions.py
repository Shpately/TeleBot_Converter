import requests


class Converter:
    def __init__(self, base, quote, amount, url):
        self.base = base
        self.quote = quote
        self.amount = amount
        self.url = url

    @staticmethod
    def get_price():
        def get_price(base, quote, amount):
            url = f"https://api.example.com/rates?base={base}&quote={quote}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if 'price' in data:
                    price = data['price']
                    converted_amount = amount * price
                    return converted_amount
                else:
                    raise ValueError(f"Invalid response format from API: {data}")
            else:
                raise ConnectionError(f"Failed to fetch data from API: {response.status_code}")