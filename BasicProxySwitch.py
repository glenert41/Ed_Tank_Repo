from urllib import request as urlrequest

PROXY_ADDRESS = '13.85.25.59:8080'
url = "http://icanhazip.com"

request = urlrequest.Request(url)
request.set_proxy(PROXY_ADDRESS,"http")

response = urlrequest.urlopen(request)



print(response.read().decode("utf8"))