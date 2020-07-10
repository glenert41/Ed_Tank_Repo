from bs4 import BeautifulSoup
import requests
import random

class ScrapeProxies:

    def __init__(self, url, proxy_amount):

        self.url = url
        self.proxy_amount = proxy_amount

    def scrape(self):

        url = self.url
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        proxy_list_raw = soup.find_all('td')
        c = 0
        proxy_list = []

        while c < self.proxy_amount * 8:
            proxy_list.append(str(proxy_list_raw[c])[4:len(proxy_list_raw[c]) - 6])
            proxy_list.append(str(proxy_list_raw[c + 1])[4:len(proxy_list_raw[c + 1]) - 6])
            c = c + 8

        #print(proxy_list)

        rand = random.randint(0, (self.proxy_amount * 2) - 1)
        if rand % 2 == 1:
            rand = rand - 1
        PROXY = str(proxy_list[rand] + ":" + proxy_list[rand + 1])
        
        return PROXY

proxy = ScrapeProxies("https://sslproxies.org", 20).scrape() # max of 20 random proxies
print(proxy)
