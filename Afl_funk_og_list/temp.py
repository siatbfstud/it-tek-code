import dht
from machine import Pin
import umqtt_robust2

templist = []
sensor1 = dht.DHT11(Pin(19))
def temperatur():
    sensor1.measure()
    tempval = sensor1.temperature()
    templist.append(tempval)