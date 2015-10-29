import http.client
import http.server
import urllib.parse
import cgi
import threading

c = http.client.HTTPConnection("127.0.0.1", 8000)

serverSetup = False;

class InputRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        
        vars = cgi.parse_qs(self.rfile.read(int(self.headers["Content-length"])))
        print(vars)
        prompt = vars[b"prompt"][0].decode("UTF-8")

        self.wfile.write(bytes(input(prompt), "UTF-8"))

def startInputRequestServer():
    global serverSetup
    inputRequestServer = http.server.HTTPServer(("127.0.0.1", 8001), InputRequestHandler)
    print("Input request server created on IP", inputRequestServer.server_address[0], "on port", inputRequestServer.server_address[1])
    serverSetup = True
    inputRequestServer.serve_forever()

t = threading.Thread(target=startInputRequestServer)
t.start()

while not serverSetup: pass

while True:
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
            code += line + "\n"

        params = urllib.parse.urlencode({"code": code})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

        c.request("POST", "", params, headers)

        response = c.getresponse().read()

        print(response)

    except:
        traceback.print_exc()