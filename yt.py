#import webbrowser
#webbrowser.open('https://www.youtube.com/watch?v=wRb12E9mEKY')

from selenium import webdriver
from time import sleep
profile=webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '13.127.185.233')
profile.set_preference('network.proxy.socks_port', 9150)


count = 0
for i in range(100):
    driver = webdriver.Firefox(profile)
    driver.get("https://www.youtube.com/watch?v=wRb12E9mEKY")
    sleep(2)
    driver.close()
    count = count+1
    print('views :'+str(count))