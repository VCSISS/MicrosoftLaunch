import http.server
import http.client
import urllib.parse
import cgi
import re
import traceback
import _wingpio as pins

c = http.client.HTTPConnection("10.79.1.51", 8001)

def getInput(prompt=""):
    global c

    c.request("GET", "",
                urllib.parse.urlencode({"prompt": prompt}),
                {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"})

    response = c.getresponse().read()

    return response.decode("UTF-8")

input = getInput

class CommandExecutingRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_respones(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
    
    def do_POST(self):
        command = self.path

        self.status_update("Client requested with type POST")

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        print("Executing===============================")

        try:
            vars = cgi.parse_qs(self.rfile.read(int(self.headers["Content-length"])))
            code = (vars[b"code"])[0]
            codeString = code.decode("UTF-8")
            
            exec(codeString)

            self.wfile.write(b"Success")
        except Exception as ex:
            traceback.print_exc()
            self.wfile.write(b"Failure")

        print("========================================")

    def status_update(self, message):
        print("STATUS:", message)
