import http.server
import mywebserver

print("Server started")
httpd = http.server.HTTPServer((mywebserver.HOST_NAME, mywebserver.PORT_NUMBER), mywebserver.MyHandler)

try:
    httpd.serve_forever()
    
except KeyboardInterrupt:
    httpd.server_close()
    print("Server closed")
