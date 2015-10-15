import http.client
import xml.etree.ElementTree as etree
import _wingpio as pins
import time

pin = 23

c = http.client.HTTPConnection("", 8000)

try:
    while True:
        # request from server (no need to request a url, just make request)
        c.request("GET", "")
        response = c.getresponse().read()

        # get number from XML
        blink = etree.fromstring(response)
        number = int(blink.text)
    
        # flash LED accordingly
        if number == 1:
            pins.output(pin, pins.HIGH)
        else:
            pins.output(pin, pins.LOW)

        time.sleep(1)

except Exception as e:
    print(str(e))
