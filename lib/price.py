import requests
import json

def get():
    # using coinbase API
    req = requests.get('https://api.coinbase.com/v2/prices/bch-usd/buy')
    json = req.json()
    bch_price = float(json['data']['amount'])
    price = 1 / bch_price
    return str(price)

def writePrice(price):
    with open('price', 'w') as f:
        f.write(price)

if __name__ == '__main__':
    price = get()
    writePrice(price)