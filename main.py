import time
import pycom
from machine import Pin
from dth import DTH

pycom.heartbeat(False)
pycom.rgbled(0x000008) # blue

def pin_handler(arg):
    print("Motion detected")
    pycom.rgbled(0x7f0000) # red
    time.sleep_ms(500)
    pycom.rgbled(0x7f7f00) # yellow

pir = Pin('G4',mode=Pin.IN,pull=Pin.PULL_UP)
pir.callback(Pin.IRQ_FALLING | Pin.IRQ_RISING, pin_handler)

th = DTH(Pin('P3', mode=Pin.OPEN_DRAIN),0)
time.sleep(2)
result = th.read()

while True:
    if result.is_valid():
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        time.sleep(1)
