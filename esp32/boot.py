# This file is executed on every boot (including wake-boot from deepsleep)
# see https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html

import uos, machine
import gc
import ujson as json
import webrepl

# function to connect to internet
def do_connect(ssid, password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


webrepl.start()
gc.collect()

# See https://www.youtube.com/watch?v=_vcQTyLU1WY
# See https://github.com/CapableRobot/SenseTemp/blob/master/software-micropython/main-mqtt.py

# read settings
settings = json.load(open("settings.json", 'r'))
# connect to internet
do_connect(ssid=settings["wifi"]["ssid"], password=settings["wifi"]["password"])
# trigger logging to adafruit io
import adafruit_io_publish