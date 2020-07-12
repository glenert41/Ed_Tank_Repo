from bs4 import BeautifulSoup
import requests
import random

# https://hidemy.name/en/proxy-list/?country=US&maxtime=1000&type=h&anon=234#list

def generate_proxy(url, proxy_amount):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    if url == "https://sslproxies.org":
        proxy_list_raw = soup.find_all('td')
        c = 0
        proxy_list = []

        while c < proxy_amount * 8:
            proxy_list.append(str(proxy_list_raw[c])[4:len(proxy_list_raw[c]) - 6])
            proxy_list.append(str(proxy_list_raw[c + 1])[4:len(proxy_list_raw[c + 1]) - 6])
            c = c + 8

        # print(proxy_list)

        rand = random.randint(0, (proxy_amount * 2) - 1)
        if rand % 2 == 1:
            rand = rand - 1
        PROXY = str(proxy_list[rand] + ":" + proxy_list[rand + 1])

        return PROXY

    # if self.url == "https://hidemy.name/en/proxy-list/?country=US&maxtime=1000&type=h&anon=234#list":

    # print(soup.find_all('table'))

    else:
        return "Invalid URL"


def scrape(request_method, url, **kwargs):
    while True:
        try:
            proxy = generate_proxy()
            print("Proxy is being used: {}".format(proxy))
            response = requests.request(request_method, url, proxies=proxy, timeout=7, **kwargs)
            break
        except:
            print("Connection error")
            pass

    return response

        # works on https://sslproxies.org


# or https://hidemy.name/en/proxy-list/?country=US&maxtime=1000&type=h&anon=234#list

proxy = generate_proxy("https://sslproxies.org", 20)  # max of 20 random proxies
print(scrape('get','https://soundcloud.com/eddison-duolo-546732382/so-many-nights-ed-tank'))
