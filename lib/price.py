import requests
import json

def get():
    # using coinbase API
    req = requests.get('https://api.coinbase.com/v2/prices/bch-usd/buy')
    json = req.json()
    bch_price = float(json['data']['amount'])
    price = round(1 / bch_price, 7)
    return price