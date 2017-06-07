import time
import pycom
from machine import Pin
from dth import DTH
from simple import MQTTClient
#
def settimeout(duration):
   pass
#
client = MQTTClient(client_id="wipy_client", server='192.168.0.100', port=1883)  #

client.settimeout = settimeout
client.connect()

pycom.heartbeat(False)
pycom.rgbled(0x000008) # blue

def pin_handler(arg):
    print("Motion detected")
    client.publish("wipy/motion", "Motion detected")
    pycom.rgbled(0x7f0000) # red
    time.sleep_ms(500)
    pycom.rgbled(0x7f7f00) # yellow

pir = Pin('G4',mode=Pin.IN,pull=Pin.PULL_UP)
pir.callback(Pin.IRQ_RISING, pin_handler)    # Pin.IRQ_FALLING | # Only detect on rising

th = DTH(Pin('P3', mode=Pin.OPEN_DRAIN),0)
time.sleep(2)
result = th.read()

while True:
    if result.is_valid():
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        time.sleep(1)
