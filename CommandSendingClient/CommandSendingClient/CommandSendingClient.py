import http.client
import urllib.parse

c = http.client.HTTPConnection("127.0.0.1", 8000)

while True:

    code = ""

    while True:
        line = input(">>> ")
        if line == ".":
            break
        code += line

    params = urllib.parse.urlencode({"code": code})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

    c.request("POST", "", params, headers)

    response = c.getresponse().read()

    print(response)