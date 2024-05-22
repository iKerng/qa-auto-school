from webdrv import chrome_114
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from time import sleep


try:
    link = 'https://suninjuly.github.io/selects1.html'
    browser = chrome_114()
    browser.get(link)

    res = int(browser.find_element(By.CSS_SELECTOR, '#num1').text) + int(browser.find_element(By.CSS_SELECTOR, '#num2').text)

    select.Select(browser.find_element(By.CSS_SELECTOR, 'select')).select_by_value(str(res))

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    sleep(5)
    browser.quit()
