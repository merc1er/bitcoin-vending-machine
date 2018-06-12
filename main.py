####################
import requests
import qrcode
from flask import Flask
from flask import render_template
####################

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# order
@app.route('/<item>')
def order(item=None):
    # fetch the correct price here
    price = 0.001
    url = 'bitcoincash:qz8zcxumuzd8fx4cxc73qlhs8kta4jv6wu9knfn567?amount='
    url += str(price)
    img = qrcode.make(url)
    img.save('static/qr.png')
    return render_template('order.html', item=item, price=price)

####################
# checking the payment

app.run(debug=True, port=666, host='127.0.0.1')