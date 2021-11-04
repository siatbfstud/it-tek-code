from machine import Pin, I2C
from tcs34725 import *


    
class rgb:
    def __init__(self):
        self.rgb_val = (0, )
        self.rgb_list = []
    def set_rgb(self, mes_val):
        self.rgb_val = mes_val
        
    def colorlist(self, rgb_list2 = list):
        self.rgb_list = rgb_list2
        
    def rgbtolist(self):
        i2c = I2C(0, scl = Pin(19), sda = Pin(18), freq = 10000)

        if i2c.scan() != []:
            sensor = TCS34725(i2c)
            sensor.gain(60)
            data = sensor.read(True)
            print(html_rgb(data))

colorsens = rgb
        

# test = html_rgb(data)
# print(test[0])
# print(type(test[0]))
# testlist = list(test)
# print(testlist)
# print(type(testlist))