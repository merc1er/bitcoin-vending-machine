####################
import requests
import qrcode
from flask import Flask, render_template
from random import randint
####################

app = Flask(__name__)

# input your Bitcoin Cash address here
your_address = 'bitcoincash:qzrcvjpplnpa6qq2dtcshmke4yl9ngdwfcyfan5vtc'


@app.route('/')
def index():
    return render_template('index.html')

# order
@app.route('/<item>')
def order(item=None):
    # fetch the correct price here
    import lib.price as price
    can_price = getprice()
    url = your_address + '?amount='
    url += str(can_price)
    img = qrcode.make(url)
    img.save('static/qr.png')
    rnd = randint(1000, 100000000)
    force_reload = '?' + str(rnd)
    return render_template('order.html', item=item, price=round(can_price, 4),
                                    exact_price=can_price, forcer=force_reload)

def getprice():
    with open('price', 'r') as f:
        price = f.readline()
    return float(price)

####################
# checking the payment
@app.route('/<item>/paid')
def payment_complete(item=None):
    # if the item is paid, dispense the can + inform user
    return render_template('paid.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
