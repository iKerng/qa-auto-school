from webdrv import chrome_114
from selenium.webdriver.common.by import By
from math import log, sin, e
from time import sleep


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = chrome_114()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    browser.switch_to.window(browser.window_handles[1])
    sleep(1)

    x = int(browser.find_element(By.CSS_SELECTOR, 'span#input_value').text)
    res = log(abs(12 * sin(x)), e).__str__()
    browser.find_element(By.CSS_SELECTOR, 'input#answer').send_keys(res)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    sleep(1)
    print(browser.switch_to.alert.text.split(' ')[-1])

finally:
    sleep(1)
    browser.quit()