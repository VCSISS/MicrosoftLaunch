import http.server
import cgi

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
            exec(code.decode("UTF-8"))
            self.wfile.write(b"Success")
        except Exception as ex:
            print("Error:")
            print(str(ex))
            self.wfile.write(b"Failure")

        print("========================================")

    def status_update(self, message):
        print("STATUS:", message)
