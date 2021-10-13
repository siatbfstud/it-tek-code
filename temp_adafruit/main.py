import mqttBotPubSub
import dht
from machine import Pin
from time import sleep

lib = mqttBotPubSub

sensor = dht.DHT11(Pin(19))

led = Pin(18, Pin.OUT, value = 0)

while True:
    try:
        if lib.m == "test":
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="streng fra bot")
            lib.m = ""

        if lib.m == "hej jarvis":
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="hej master")
            lib.m = ""

        if lib.m == "fortæl en joke":
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="virksomhedsfaget kek")
            lib.m = ""

        if lib.m == "fortæl en joke mere":
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="Husk at indsætte joke her...")
            lib.m = ""

        if lib.m == "tempc":
            sensor.measure()
            temp = sensor.temperature()
            sleep(1)
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="Temperatur: %3.1f C" % temp)
            lib.m = ""
            if temp > 30:
                for x in range(4):
                    lib.client.publish(topic=lib.mqtt_pub_feedname, msg="Det er for varmt!!!")
                    lib.m = ""
            elif temp < 20:
                for y in range(4):
                    lib.client.publish(topic=lib.mqtt_pub_feedname, msg="Det er for koldt!!!")
                    lib.m = ""
        if lib.m == "fugt":
            sensor.measure()
            hum = sensor.humidity()
            sleep(1)
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="Fugtigheden: %3.1f procent" % hum)
            lib.m = ""
        if lib.m == "tænd lys":
            led.value(True)
        if lib.m == "sluk lys":
            led.value(False)
        if lib.m == "lys":
            led.value(not led.value())

        lib.client.check_msg()

    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        lib.client.disconnect()
        lib.sys.exit()
