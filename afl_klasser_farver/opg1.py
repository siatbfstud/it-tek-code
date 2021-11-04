import umqtt_robust2
from machine import Pin
import dht
from time import sleep_ms, sleep

lib = umqtt_robust2
sensor = dht.DHT11(Pin(19))

class sensor_class:
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
    def set_temp(self, mes_val:int):
        self.temperature = mes_val
    def set_hum(self, mes_val:int):
        self.hum = mes_val
    
print(sensor_class.description)
my_sens = sensor()


def temp():
    sleep(1)
    sensor.measure()
    return sensor.temperature()

my_sens.set_temperature(temp())

def func():
    print("Measured temp: ", mysensor.temerature)
func()

