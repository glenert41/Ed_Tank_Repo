from selenium import webdriver
import time

from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list() #this will create proxy list


PROXY = proxies[0].get_address()


webdriver.DesiredCapabilities.CHROME['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,

"proxyType":"MANUAL",

}


driver = webdriver.Chrome("/Users/grahamlenert/Downloads/chromedriverowen")
site = driver.get("https://soundcloud.com/eddison-duolo-546732382/so-many-nights-ed-tank")

for x in range(1, 5):

    play_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a')
time.sleep(1)
play_btn.click()
time.sleep(5)
driver.refresh()
time.sleep(1)
