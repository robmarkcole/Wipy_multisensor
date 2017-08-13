from machine import UART
import os
import gc
from network import WLAN
from mqtt import MQTTClient

gc.enable()  # enable auto garbage collection

wlan = WLAN() # we call the constructor without params
uart = UART(0, 115200)
os.dupterm(uart)

wlan = WLAN(mode=WLAN.STA)
wlan.scan()

wlan.connect(ssid='YOURWiFi',
             auth=(WLAN.WPA2, 'YOURWiFi_pass'))

while not wlan.isconnected():
    pass

print(wlan.ifconfig())

####### MQTT setup

def settimeout(duration):
   pass

mqtt = MQTTClient(client_id="wipy_client",
                  server='192.168.0.30',
                  port=1883)

mqtt.settimeout = settimeout
mqtt.connect()
