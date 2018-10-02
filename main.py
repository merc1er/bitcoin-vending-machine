################################################################################
import requests
import qrcode
from flask import Flask, render_template
from random import randint
################################################################################

app = Flask(__name__)

# Global variables
with open('address', 'r') as f:
    your_address = f.readline().strip()
html_address = your_address.replace(':', '%3A')


@app.route('/')
def index():
    return render_template('index.html')

# order
@app.route('/<item>')
def order(item=None):
    import lib.price as price
    can_price = getprice()
    url = your_address + '?amount='
    url += str(can_price) # appending the amount
    img = qrcode.make(url)
    img.save('static/qr.png')
    rnd = randint(1000, 100000000) # append to the image so it gets hard loaded
    force_reload = '?' + str(rnd)
    return render_template('order.html', item=item, price=round(can_price, 4),
                                            exact_price=can_price,
                                            forcer=force_reload,
                                            html_address=html_address)

def getprice():
    with open('price', 'r') as f:
        price = f.readline()
    if price == '': # in case the file is empty
        print('empty price') # test
        import lib.price as price
        print('imported') # test
        price.get()
        print('got') # test
        return getprice()
    return float(price)

####################
# Checking the payment
@app.route('/<item>/paid')
def payment_complete(item=None):
    # the item is now paid
    import lib.dispense as dispense
    dispense.dispense(item)
    return render_template('paid.html')

####################
# Error page
@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
