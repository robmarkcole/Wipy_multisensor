import pycom
import time
from machine import Pin
from dth import DTH

# The callback if motion on PIR
def pin_handler(arg):
    print("Motion detected")
    mqtt.publish("wipy/Motion", "Motion detected")
    pycom.rgbled(0x7f0000) # red
    time.sleep_ms(500)
    pycom.rgbled(0x7f7f00) # yellow

pycom.heartbeat(False)
pycom.rgbled(0x000008) # blue

pir = Pin('G4',mode=Pin.IN,pull=Pin.PULL_UP)
pir.callback(Pin.IRQ_RISING, pin_handler)    # Only detect on rising

th = DTH(Pin('P3', mode=Pin.OPEN_DRAIN),0)
time.sleep(2)

while True:
    pycom.rgbled(0x000008) # blue
    time.sleep(1)
    result = th.read()
    if result.is_valid():
        pycom.rgbled(0x001000) # green
        gc.collect()   # perform garbage collection
        print(gc.mem_free())
        mqtt.publish("wipy/Memory", str(gc.mem_free()))

        print("Temperature: %d C" % result.temperature)
        mqtt.publish("wipy/Temperature", str(result.temperature))

        print("Humidity: %d %%" % result.humidity)
        mqtt.publish("wipy/Humidity", str(result.humidity))
    time.sleep(1)
