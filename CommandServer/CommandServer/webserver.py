import http.server
import sys

class CommandServer(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

    def do_GET(self):
        line = ""
        code = ""

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        while True:
            line = input(">>> ")
            if line == ".":
                break
            code += line

        self.wfile.write(bytearray(code, "UTF-8"))

        print("Send code to client")