def do_connect(ssid, password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting")
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print("network config", sta_if.ifconfig())

do_connect("4-ManStack", "Jasmin123")


import webrepl
webrepl.start()
