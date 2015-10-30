from __future__ import print_function
import BaseHTTPServer
import httplib
import urlparse
import urllib
import traceback

ioc = httplib.HTTPConnection("10.0.0.10", 8001)

def get_input(prompt=""):
    global ic

    ioc.request("GET", "",
              urllib.urlencode({"prompt": prompt}),
              {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"})

    response = ioc.getresponse().read()

    return response.decode("UTF-8")


def remote_print(*objects):
    string = "".join([str(i) for i in objects])

    ioc.request("POST", "",
                urllib.urlencode({"print": string}),
                {"Content-type": "application/x-ww-form-urlencoded", "Accept": "text/plain"})

    ioc.getresponse()

input = get_input


class CommandExecutingRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
    
    def do_POST(self):
        global print
        try:
            self.status_update("Client requested with type POST")

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            old_print = print
            print = remote_print

            print("Executing===============================")

            vars = urlparse.parse_qs(self.rfile.read(int(self.headers["Content-length"])))
            code = (vars[b"code"])[0]
            codeString = code.decode("UTF-8")
            
            exec(codeString)

            self.wfile.write(b"Success")

        except Exception as ex:
            traceback.print_exc(file=self.wfile)

        finally:
            print("========================================")
            print = old_print

    def status_update(self, message):
        print("STATUS:", message)
