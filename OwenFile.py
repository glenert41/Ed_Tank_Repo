import requests
import random
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
#rom Random_Proxy_Lib import *

'''
generate_proxy()
PROXY = check_proxy('get','https://soundcloud.com/eddison-duolo-546732382/so-many-nights-ed-tank')

#PROXY = "51.15.84.185:3128"
'''

'''
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
'''
'''

webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,

    "proxyType": "MANUAL",

}



#driver = webdriver.Chrome("/Users/owenmckenney/Downloads/chromedriver")
#site = driver.get("https://soundcloud.com/eddison-duolo-546732382/so-many-nights-ed-tank")

for x in range(1, 10):
    #Applies new proxy
    generate_proxy()
    PROXY = check_proxy('get', 'https://soundcloud.com/eddison-duolo-546732382/so-many-nights-ed-tank')

    driver = webdriver.Chrome("/Users/owenmckenney/Downloads/chromedriver")

    #redefines the Xpaths for the buttons
    SoManyNights = driver.get("https://soundcloud.com/eddison-duolo-546732382/so-many-nights-ed-tank")
    low_play_btn = driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div[3]/button[2]')

    #Opens the Window, Plays, Closes the Window, and prints the user agent
    time.sleep(2)
    low_play_btn.click()
    time.sleep(5)
    driver.close()
    #r = requests.get("http://httpbin.org/user-agent", headers=random.choice(vars))
    #print(r.content)

'''

'''
# graham method

#list of random user agents, and chooses a random one
h1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
h2 = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"}
h3 = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"}
h4 = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"}
h5 = {"User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
h6 = {"User-Agent" : "Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36"}
h7 = {"User-Agent" : "Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7412.EU"}
h8 = {"User-Agent" : "Mozilla/5.0 (PlayStation Vita 3.61) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2"}
h9 = {"User-Agent" : "Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko)"}
h10 = {"User-Agent" : "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate)"}
h11 = {"User-Agent" : "Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+"}
h12 = {"User-Agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36"}
vars = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12]
userH = random.choice(vars)

#sets the changed user agent
opts = Options()
opts.add_argument("user-agent=" + str(userH))

for x in range(0, 5):
    #Applies the changed user agent
    driver = webdriver.Chrome("/Users/owenmckenney/Downloads/chromedriver", options=opts)

    #redefines the Xpaths for the buttons
    SoManyNights = driver.get("https://soundcloud.com/eddison-duolo-546732382/so-many-nights-ed-tank")
    low_play_btn = driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div[3]/button[2]')

    #Opens the Window, Plays, Closes the Window, and prints the user agent
    time.sleep(2)
    low_play_btn.click()
    time.sleep(10)
    driver.close()
    r = requests.get("http://httpbin.org/user-agent", headers=random.choice(vars))
    print(r.content)

'''

import requests
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from datetime import datetime

chrome_options = Options()
chrome_options.add_argument("--headless")

SongDuration = 4

def SoManyNights():
    SoManyNights = driver.get("https://soundcloud.com/eddison-duolo-546732382/so-many-nights-ed-tank")
    high_play_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a')
    high_play_btn.click()
    time.sleep(SongDuration)
    low_pause_btn = driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div[3]/button[2]')
    low_pause_btn.click()
    time.sleep(1)

def NewTab(url):

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url)
    time.sleep(1)

def PlayandStop():
    high_play_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a')
    high_play_btn.click()
    time.sleep(SongDuration)
    low_pause_btn = driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div[3]/button[2]')
    low_pause_btn.click()


def CloseAllWindows():
    driver.quit()

for x in range (0, 648): # 648 for 9hour play time

    #Option to run headless
    driver = webdriver.Chrome("/Users/owenmckenney/Downloads/chromedriver", options=chrome_options)

    #Option to run with head
    #driver = webdriver.Chrome("/Users/owenmckenney/Downloads/chromedriver")

    SoManyNights()

    NewTab('https://soundcloud.com/eddison-duolo-546732382/lil-pacco-ft-zay2x-fullclip')
    PlayandStop()
    NewTab('https://soundcloud.com/eddison-duolo-546732382/lil-pacco-ft-jayv2')
    PlayandStop()
    NewTab('https://soundcloud.com/eddison-duolo-546732382/lil-pacco-riptessa')
    PlayandStop()
    NewTab('https://soundcloud.com/eddison-duolo-546732382/free-madison-rnw-ed')
    PlayandStop()
    NewTab('https://soundcloud.com/eddison-duolo-546732382/rnw-ed-next-up')
    PlayandStop()
    NewTab('https://soundcloud.com/eddison-duolo-546732382/ed-mama-is-proud-of-me')
    PlayandStop()

    CloseAllWindows()

    time.sleep(2)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
