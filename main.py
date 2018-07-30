####################
import requests
import qrcode
from flask import Flask, render_template
####################

app = Flask(__name__)

# input your Bitcoin Cash address here
your_address = 'bitcoincash:qz8zcxumuzd8fx4cxc73qlhs8kta4jv6wu9knfn567'


@app.route('/')
def index():
    return render_template('index.html')

# order
@app.route('/<item>')
def order(item=None):
    # fetch the correct price here
    import lib.price as price
    can_price = price.get()
    url = your_address + '?amount='
    url += str(can_price)
    img = qrcode.make(url)
    img.save('static/qr.png')
    return render_template('order.html', item=item, price=round(can_price, 4))

####################
# checking the payment
@app.route('/<item>/paid')
def payment_complete(item=None):
    # if the item is paid, dispense the can + inform user
    return render_template('paid.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')