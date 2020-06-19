from time import sleep
from simple_mqtt import MQTTClient
from machine import Pin
from dht import DHT22
import socket

# See https://www.youtube.com/watch?v=_vcQTyLU1WY

# your server needs a STATIC IP ADDRESS!!!

SERVER = "192.168.0.10"  # MQTT Server Address (Change to the IP address of your Pi)
CLIENT_ID = 'ESP32_DHT22_Sensor'
TOPIC = b'temp_humidity'

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()   # Connect to MQTT broker

# CHECK HERE THE PIN YOU USE!!!!
# DHT-22 on GPIO 14 (input with internal pull-up resistor)
# This model of ESP8266 on D5 == GPIO 14
# on ESP32 D5 is GPIO 5
sensor = DHT22(Pin(5, Pin.IN, Pin.PULL_UP))   

while True:
    try:
        sensor.measure()   # Poll sensor
        t = sensor.temperature()
        h = sensor.humidity()
        if isinstance(t, float) and isinstance(h, float):  # Confirm sensor results are numeric
            msg = (b'{0:3.1f},{1:3.1f}'.format(t, h))
            client.publish(TOPIC, msg)  # Publish sensor data to MQTT topic
            print(msg)
        else:
            print('Invalid sensor readings.')
    except OSError:
        print('Failed to read sensor.')
    sleep(4)