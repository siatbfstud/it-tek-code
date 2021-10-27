import umqtt_robust2
from machine import Pin
import dht
from opg3 import randomJoke
import temp
from time import sleep_ms, sleep

lib = umqtt_robust2
sensor = dht.DHT11(Pin(19))
led = Pin(18, Pin.OUT, value = 0)

while True:
    sleep_ms(500)
    besked = lib.besked
    if lib.c.is_conn_issue():
        while lib.c.is_conn_issue():
            lib.c.reconnect()
        else:
            lib.c.resubscribe()
    try:
        if besked == "test":
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="streng fra bot")
            lib.besked = ""

        if besked == "hej jarvis":
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="hej master")
            lib.besked = ""

        if besked == "fortæl en joke":
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="virksomhedsfaget kek")
            lib.besked = ""

        if besked == "fortæl en joke mere":
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="Husk at indsætte joke her...")
            lib.besked = ""

        if besked == "tempc":
            sensor.measure()
            temp = sensor.temperature()
            sleep(0.1)
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="Temperatur: %3.1f C" % temp)
            lib.besked = ""
            if temp > 30:
                for x in range(4):
                    lib.c.publish(topic=lib.mqtt_pub_feedname, msg="Det er for varmt!!!")
                    lib.besked = ""
            elif temp < 20:
                for y in range(4):
                    lib.c.publish(topic=lib.mqtt_pub_feedname, msg="Det er for koldt!!!")
                    lib.besked = ""
        
        if besked == "fugt":
            sensor.measure()
            hum = sensor.humidity()
            sleep(1)
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="Fugtigheden: %3.1f procent" % hum)
            lib.besked = ""
        
        if besked == "tænd lys":
            led.value(True)
        if besked == "sluk lys":
            led.value(False)
        if besked == "lys":
            led.value(not led.value())
        
        if besked == "random joke":
            randomJoke()
        
        if besked == "10 temp":
            for a in range(10):
                temp.temperatur()
                sleep(1)
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="10 temperaturer tilføjet")
            lib.besked = ""
            
        if besked == "tilføj temp":
            temp.temperatur()
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="Temperatur tilføjet")
            lib.besked = ""
            
        if besked == "vis temp":
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="".join(str(temp.templist)))
            lib.besked = ""

    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        lib.client.disconnect()
        lib.sys.exit()
    except OSError as e:
        print('Failed to read sensor.')
    lib.c.check_msg()
    lib.c.send_queue()
lib.c.disconnect()


