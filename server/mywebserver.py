# Add your code here to run in your startup task

import http.server

HOST_NAME = ""
PORT_NUMBER = 8000

number = 0

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/xml")
        self.end_headers()

    def do_GET(self):
        global number
        
        self.send_response(200)
        self.send_header("Content-type", "text/xml")
        self.end_headers()

        self.wfile.write(b"<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
        
        # write number back to client (1 or 0), toggled each time
        self.wfile.write(bytes("<blink>" + str(number) + "</blink>", "UTF8"))

        number = 1 if number == 0 else 0
