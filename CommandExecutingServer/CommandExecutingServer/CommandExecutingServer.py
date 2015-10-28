import http.server
import webserver

httpd = http.server.HTTPServer(("", 8000), webserver.CommandExecutingRequestHandler)
print("Started server on IP", httpd.server_address[0], "on port", httpd.server_address[1])
httpd.serve_forever()