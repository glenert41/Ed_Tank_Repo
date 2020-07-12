from bs4 import BeautifulSoup
import requests
from random import choice

def generate_proxy():
    response = requests.get("https://sslproxies.org/")
    soup = BeautifulSoup(response.content, 'html5lib')
    proxy = {'https': choice(list(map(lambda x: x[0] + ':' + x[1], list(zip(map(lambda x: x.text,
            soup.findAll('td')[::8]), map(lambda x: x.text, soup.findAll('td')[1::8]))))))}
    return proxy

def check_proxy(request_method, url, **kwargs):
    while True:
        try:
            proxy = generate_proxy()
            print("Proxy is being used: {}".format(proxy))
            response = requests.request(request_method, url, proxies=proxy, timeout=7, **kwargs)
            break
        except:
            print("Connection error")
            pass

    return proxy.get("https")

# works on https://sslproxies.org
generate_proxy()
proxy = check_proxy('get','https://soundcloud.com/eddison-duolo-546732382/so-many-nights-ed-tank')
print(proxy)
