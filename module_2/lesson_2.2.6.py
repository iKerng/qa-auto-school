from webdrv import chrome_114
from selenium.webdriver.common.by import By
from math import sin, log, e
from time import sleep


try:
    # Открыть страницу http://suninjuly.github.io/execute_script.html
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = chrome_114()
    browser.get(link)
    sleep(1)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)

    # Посчитать математическую функцию от x (сама функция остаётся неизменной).
    res = log(abs(12 * sin(x)), e).__str__()

    browser.find_element(By.CSS_SELECTOR, 'input#answer').send_keys(res)

    browser.find_element(By.CSS_SELECTOR, 'label[for="robotCheckbox"]').click()
    element = browser.find_element(By.CSS_SELECTOR, 'label[for="robotsRule"]')
    browser.execute_script('return arguments[0].scrollIntoView(true)', element)
    element.click()
    sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    browser.execute_script('return arguments[0].scrollIntoView(true)', button)
    button.click()


finally:
    sleep(5)
    browser.quit()