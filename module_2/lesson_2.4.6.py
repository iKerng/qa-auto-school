from webdrv import chrome_114
from selenium.webdriver.common.by import By
from math import log, sin, e
from time import sleep
from os import path


try:
    link = 'http://suninjuly.github.io/cats.html'
    browser = chrome_114()
    browser.get(link)
    browser.find_element(By.ID, "button")

finally:
    sleep(5)
    browser.quit()


