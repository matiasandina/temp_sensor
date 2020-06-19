from time import sleep
from simple_mqtt import MQTTClient
from machine import Pin
from dht import DHT22
import socket
import ujson as json

# See https://www.youtube.com/watch?v=_vcQTyLU1WY
# See https://github.com/CapableRobot/SenseTemp/blob/master/software-micropython/main-mqtt.py

# read settings
settings = json.load(open("settings.json", 'r'))


client = MQTTClient(
    client_id = settings['device']['name'], 
    server    = settings['mqtt']['server'], 
    user      = settings['mqtt']['user'],
    password  = settings['mqtt']['key'],
    ssl=False
)
# Connect to MQTT broker
client.connect()   
print("MQTT Client : Connected")

# CHECK HERE THE PIN YOU USE!!!!
# DHT-22 on GPIO 14 (input with internal pull-up resistor)
# This model of ESP8266 on D5 == GPIO 14
# This model of ESP32 on D5 == GPIO 5
sensor = DHT22(Pin(5, Pin.IN, Pin.PULL_UP))   
# we will send data in csv format
topic_temp = settings['mqtt']['feed'] + "-temperature"
topic_hum = settings['mqtt']['feed'] + "-humidity"

while True:
    try:
        # Poll sensor
        sensor.measure()   
        t = sensor.temperature()
        h = sensor.humidity()
        if isinstance(t, float) and isinstance(h, float):  # Confirm sensor results are numeric
            # Publish sensor data to MQTT topic
            client.publish(topic_temp, b'{0:3.1f}'.format(t))
            client.publish(topic_hum, b'{0:3.1f}'.format(h))  
            msg = (b'{0:3.1f},{1:3.1f}'.format(t, h))
            print(msg)
        else:
            print('Invalid sensor readings.')
    except OSError:
        print('Failed to read sensor.')
    sleep(settings['mqtt']['sleep'])