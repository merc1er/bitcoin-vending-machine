####################
import requests
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
    return render_template('order.html', item=item)

app.run(debug=True, port=666, host='127.0.0.1')