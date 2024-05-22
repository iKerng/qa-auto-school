from webdrv import chrome_114
from selenium.webdriver.common.by import By
from math import log, sin, e
from time import sleep

try:
    # Открыть страницу http://suninjuly.github.io/get_attribute.html.
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = chrome_114()
    browser.get(link)
    sleep(1)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = int(browser.find_element(By.CSS_SELECTOR,'img#treasure').get_attribute('valuex'))

    # Посчитать математическую функцию от x (сама функция остаётся неизменной).
    res = log(abs(12 * sin(x)), e).__str__()

    # Ввести ответ в текстовое поле.
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(res)

    # Отметить checkbox "I'm the robot".
    browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox').click()

    # Выбрать radiobutton "Robots rule!".
    browser.find_element(By.CSS_SELECTOR, 'input#robotsRule').click()


finally:
    # Нажать на кнопку Submit.
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    sleep(5)

    # закрываем браузер
    browser.quit()
