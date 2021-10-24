import umqtt_robust2
import random
lib = umqtt_robust2
def randomJoke():
    jokelist = ["joke1", "joke2", "joke3"]
    lib.c.publish(topic=lib.mqtt_pub_feedname, msg=random.choice(jokelist))
    lib.besked = ""