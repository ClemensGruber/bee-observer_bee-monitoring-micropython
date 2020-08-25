import machine
from network import WLAN
import time
import pycom

# Disable Hearbeat
pycom.heartbeat(False)

# configure WLAN in station mode
print("Starting Wifi connection ", end='')
wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid='[your-ssid]', auth=(WLAN.WPA2, '[your-pw]'))
while not wlan.isconnected():
    time.sleep(3)
    print('.', end='')
print()
print("Wifi Connection established")
print(wlan.ifconfig())
print()

# make the LED light up in blue color
pycom.rgbled(0x000011)
time.sleep(2)
