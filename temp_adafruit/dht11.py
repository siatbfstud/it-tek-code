from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(19))

test = "Heyo"

while True:
    try:
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        f = temp * (9/5) + 32
        print("Temperatur: ", temp, "Celsius")
        print("Temperatur: ", f, "Fahrenheit")

        hum = sensor.humidity()
        print("Fugtigheden er ", hum, "%")

    except OSError as e:
        print("failed")
