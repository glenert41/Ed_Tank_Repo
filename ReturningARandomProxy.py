from urllib import request as urlrequest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome("/Users/grahamlenert/Downloads/chromedriverowen")
EdSoundcloud = "https://soundcloud.com/eddison-duolo-546732382"
url = EdSoundcloud
GrahamUserAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"

#PROXY_ADDRESS = '13.85.25.59:8080' #This is the "Random Address"




opts = Options()
opts.add_argument(GrahamUserAgent)

driver = webdriver.Chrome(chrome_options=opts)