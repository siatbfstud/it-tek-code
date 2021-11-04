from time import ticks_ms, sleep
from machine import Pin, TouchPad

interval = 1000

pTime = 0

red = Pin(19, Pin.OUT)
yellow = Pin(18, Pin.OUT)
green = Pin(17, Pin.OUT)

rstate = 0
ystate = 0
gstate = 0

tred = TouchPad(Pin(27))
tyellow = TouchPad(Pin(33))
tgreen = TouchPad(Pin(32))

while True:
    cTime = ticks_ms()
    if(tred.read() < 200 and cTime - pTime > interval):
        pTime = cTime
        if(rstate == 1):
            rstate = 0
        else:
            rstate = 1
        red.value(rstate)
            
    if(tyellow.read() < 200 and cTime - pTime > interval):
        pTime = cTime
        if(ystate == 1):
            ystate = 0
        else:
            ystate = 1
        yellow.value(ystate)
            
    if(tgreen.read() < 200 and cTime - pTime > interval):
        pTime = cTime
        if(gstate == 1):
            gstate = 0
        else:
            gstate = 1
        green.value(gstate)
    

    