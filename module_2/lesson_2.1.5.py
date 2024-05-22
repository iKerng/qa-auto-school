from webdrv import chrome_114
from selenium.webdriver.common.by import By
from math import log, sin, e
from time import sleep

try:
    # Открыть страницу https://suninjuly.github.io/math.html
    link = 'https://suninjuly.github.io/math.html'
    browser = chrome_114()
    browser.get(link)
    sleep(1)

    # Считать значение для переменной x.
    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)

    # Посчитать математическую функцию от x (код для этого приведён ниже).
    res = log(abs(12 * sin(x)), e)
    # print(res)

    # Ввести ответ в текстовое поле.
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(res.__str__())

    # Отметить checkbox "I'm the robot".
    browser.find_element(By.CSS_SELECTOR, 'label[for="robotCheckbox"]').click()

    # Выбрать radiobutton "Robots rule!".
    browser.find_element(By.CSS_SELECTOR, 'label[for="robotsRule"]').click()


finally:
    # Нажать на кнопку Submit.
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    sleep(3)

    # закрываем браузер
    browser.quit()
