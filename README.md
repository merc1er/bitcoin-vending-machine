# Bitcoin (BCH) vending machine

*Bitcoin Vending Machine is a simple software that will turn your micro-computer into a fully functional vending machine.*

[![showcase](bitcoin-vending.jpg)](https://www.youtube.com/watch?v=jCm6xKr1zkM)

## Installation

*Tested on several UNIX-like operating systems. Works on ARM.*

For now, this is a browser-based application which means the app is going to run on a full-screen browser.

Hardware requirement: *rest to come* (for now a touch screen will suffice)  
Software requirement: this is a Python3 app. Then download the required libraries with the following command:

```shell
pip3 install -i requirements.txt
```

Start the Flask server with:

```shell
sudo python3 main.py
```

And open up 127.0.0.1:5000

## Hardware

- Raspberry Pi 3
- LCD 3.5inch RPi display
    - 480x320 pixels

![hardware](http://image.noelshack.com/fichiers/2018/24/2/1528771434-hardware.jpeg)

## Todo list

- [ ] JavaScript page loader

## Future improvements

- Hardware design
- Addresses generated from xpub