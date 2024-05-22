from webdrv import chrome_114
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin, e
from time import sleep
from os import path


try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = chrome_114()
    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), '100'))

    # Нажать на кнопку "Book"
    browser.find_element(By.CSS_SELECTOR, 'button#book').click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    browser.implicitly_wait(5)
    x = int(browser.find_element(By.CSS_SELECTOR, 'span#input_value').text)
    res = log(abs(12*sin(x)), e).__str__()
    browser.find_element(By.CSS_SELECTOR, 'input#answer').send_keys(res)
    button = browser.find_element(By.CSS_SELECTOR, 'button#solve')
    browser.execute_script('return arguments[0].scrollIntoView(true)', button)
    button.click()
    print(browser.switch_to.alert.text.split(' ')[-1])

finally:
    sleep(1)
    browser.quit()






