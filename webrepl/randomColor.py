from machine import Pin, PWM
from random import randint
from time import sleep
r = PWM(Pin(18))
g = PWM(Pin(5))
b = PWM(Pin(19))
def newColor():
    k = 0
    while k <= 5:
        r.duty(randint(0, 1023))
        g.duty(randint(0, 1023))
        b.duty(randint(0, 1023))
        sleep(0.2)
        k = k + 1

    print("GO!")
