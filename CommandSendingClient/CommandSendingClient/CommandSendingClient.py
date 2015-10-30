import http.client
import http.server
import urllib.parse
import threading
import traceback

ip = input("Enter IP address> ")

c = http.client.HTTPConnection(ip, 8000)

print("Created connection (may not be functional)")

serverSetup = False;

class IORequestHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        params = urllib.parse.parse_qs(self.rfile.read(int(self.headers["Content-length"])))
        
        if b"prompt" in params:
           prompt = params[b"prompt"][0].decode("UTF-8")

           self.wfile.write(bytes(input(prompt), "UTF-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        params = urllib.parse.parse_qs(self.rfile.read(int(self.headers["Content-length"])))

        if b"print" in params:
            string = params[b"print"][0].decode("UTF-8")

            print(str(string))

    def log_message(self, format, *args):
        return

def startIORequestServer():
    global serverSetup
    ioRequestServer = http.server.HTTPServer(("", 8001), IORequestHandler)
    print("IO request server created on IP", ioRequestServer.server_address[0], "on port", ioRequestServer.server_address[1])
    serverSetup = True
    ioRequestServer.serve_forever()

t = threading.Thread(target=startIORequestServer)
t.start()

while not serverSetup: pass

running = True

while running:
    code = ""
    
    try:

        while True:
            line = input(">>> ")
            if line == ".":
                break
            elif line == "\\":
                code = ""
                print("Reset")
                continue
            elif line == "dofile":
                file = input("Filename> ")
                f = open(file)
                code = "\n".join(f.readlines())
                break
            elif line == "exit":
                running = False
                break

            code += line + "\n"

        params = urllib.parse.urlencode({"code": code})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

        c.request("POST", "", params, headers)

        response = c.getresponse().read()

        print(response.decode("UTF-8"))

    except:
        traceback.print_exc()