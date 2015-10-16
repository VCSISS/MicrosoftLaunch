import http.client
import xml.etree.ElementTree as etree
import _wingpio as pins
import time

pin = 23

print("started")

c = http.client.HTTPConnection("", 8000)

print("got connection")

try:
    while True:
        print("looping")
        # request from server (no need to request a url, just make request)
        c.request("GET", "")
        response = c.getresponse().read()
        print("got response")

        # get number from XML
        blink = etree.fromstring(response)
        number = int(blink.text)
    
        print("got number")

        # flash LED accordingly
        if number == 1:
            pins.output(pin, pins.HIGH)
        else:
            pins.output(pin, pins.LOW)

        print("flashed LED")

        time.sleep(1)

except Exception as e:
    print(str(e))
