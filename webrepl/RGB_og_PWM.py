from machine import PWM, Pin
from time import sleep

freq = 5000
start_duty = 1023
r = PWM(Pin(18), freq, start_duty)
g = PWM(Pin(5), freq, start_duty)
b = PWM(Pin(19), freq, start_duty)

def colorPWM():
    while True:
        for cycle in range(1023):
            r.duty(cycle)
            g.duty(cycle)
            #print("r+g: ", cycle)
            sleep(0.005)

        for cycle in range(1023):
            b.duty(cycle)
            r.duty(cycle)
            #print("r+b: ", cycle)
            sleep(0.005)



