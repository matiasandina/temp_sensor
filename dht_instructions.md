# Temperature & Humidity Station

We will build a room temperature and humidity sensing station using

* ESP32 or ESP8266 board
* Temp/Hum sensor


### Step 1

Follow the tutorial with some things 

* Make sure your USB cable is able to send data and power

```
dmesg | grep ttyUSB0
```

Will return nothing if your cable is garbage (power only).

Note that if you are using an ESP8226, your command will be slightly different. Here's the command to flash this micropython ("Downloads/esp8266-20191220-v1.12.bin") onto the ESP.


```
esptool.py --port /dev/ttyUSB0 write_flash 0x000000 "Downloads/esp8266-20191220-v1.12.bin"
```


https://www.youtube.com/watch?v=w15-EQASP_Y


If you rename the mqtt file from `simple.py` to `simple_mqtt.py`, you need to change the import line to:

```
from umqtt.simple_mqtt import MQTTClient
```

> Note: The ESP8266 will only be able to detect WiFi signals in the 2.4 GHz range.