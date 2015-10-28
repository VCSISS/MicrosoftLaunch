import http.server
import webserver

httpd = http.server.HTTPServer(("127.0.0.1", 8000), webserver.CommandServer)
print("Server started on IPv4", httpd.server_address[0], "on port", httpd.server_address[1])
httpd.serve_forever()