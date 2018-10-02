from time import sleep

def dispense(item):
    """ Dispenses the correct item
    """
    from gpiozero import LED
    led = LED(21) # row 21 used (anode)
    led.on()
    sleep(5)
    led.off()
