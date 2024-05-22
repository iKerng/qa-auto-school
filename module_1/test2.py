import time
from webdrv import browser
import math
from selenium.webdriver.common.by import By

# link = "https://web-qa2.testqa.tech/"
# link = "http://suninjuly.github.io/find_link_text"
link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    ls_params = ['Ivan', 'Petrov', 'Smolensk', 'Russia']
    for i in range(len(elements)):
        elements[i].send_keys(ls_params[i])

    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
