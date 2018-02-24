from selenium import webdriver
from pyvirtualdisplay import Display
from time import sleep

display = Display(visible=0, size=(800, 600))
display.start()

count = 0
for i in range(2):
    driver = webdriver.Firefox()
    driver.get("https://www.youtube.com/watch?v=wRb12E9mEKY")
    sleep(2)
    driver.close()
    count = count+1
    print('views :'+str(count))
