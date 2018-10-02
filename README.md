# Bitcoin (BCH) vending machine

*Bitcoin Vending Machine is a simple software that will turn your micro-computer into a fully functional vending machine.*

v0.2.1

[![showcase](http://image.noelshack.com/fichiers/2018/40/2/1538465805-img-3565.jpg)](https://www.youtube.com/watch?v=O7LLYY2s3MA&feature=youtu.be)

## Installation

For now, this is a browser-based application which means the app is going to run on a full-screen browser.

Software requirement: this software is meant to be run on [Raspbian Stretch](https://www.raspberrypi.org/downloads/raspbian/) or later.  
⚠️ Note: in order to check payments, a stable internet connection is required.

```shell
git clone https://github.com/BUYMERCIER/bitcoin-vending-machine
cd bitcoin-vending-machine
pip3 install -r requirements.txt
vi address # input your Bitcoin Cash address here
python3 main.py
```

Then open up 127.0.0.1:5000 in your browser.

## Development

### Todo list

- [ ] JavaScript page loader
- [ ] Check different APIs
- [ ] Display error page if no internet connection/API down

### Future improvements

- Addresses generated from xpub
