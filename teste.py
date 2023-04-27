from urllib import request, parse

header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "cookie": "__cf_bm=9RJnrO6isBDMfPL3BxHse0sUy8FQP8ltQXCW3r8iz.M-1682604539-0-Acv826j/mNHbC1EzrXWfwG7JjlUQTWNDv08urBYkavVrA/ZeRzRdCI3EvBOJaI84ZrbPhgmdRRaROc/h2G48KhCWqZc6wPjuX4aLHODKp4G9",
}

dados = {
    "login-username": "Heartfilia",
    "login-password": ""
}

dados = parse.urlencode(dados).encode()

req = request.Request(
    "https://www.habblive.in/", headers=header, data=dados)
res = request.urlopen(req)

html = res.read()
print(html)
