import http.client

def status_update(message): print("STATUS:", message)

try:
    c = http.client.HTTPConnection("127.0.0.1", 8000)
    
    status_update("Set up connection with server")

    while True:
        status_update("Requesting code from server")

        c.request("GET", "")

        response = c.getresponse().read()
        
        status_update("Received code from server")

        print("Executing=============================")
        
        exec(response)

        print("======================================")

except Exception as ex:
    print(str(ex))