import dht
import machine
import time
sensor = dht.DHT22(machine.Pin(5))
while True:
    try:
        # Poll sensor
        sensor.measure()   
        t = sensor.temperature()
        h = sensor.humidity()
        if isinstance(t, float) and isinstance(h, float):  
            #print(t)
            #print(h)  
            msg = (machine.RTC().datetime(),t, h)
            print(msg)
        else:
            print('Invalid sensor readings.')
    except OSError:
        print('Failed to read sensor.')
    time.sleep(10)

