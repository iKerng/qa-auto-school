from webdrv import chrome_114
from selenium.webdriver.common.by import By
from time import sleep
from os import path


try:
    # Открыть страницу http://suninjuly.github.io/file_input.html
    link = 'http://suninjuly.github.io/file_input.html'
    browser = chrome_114()
    browser.get(link)

    # создаю словарь со списком полей и их значением для заполнения
    dict = {
        'First name': 'Ivan'
        , 'Last name': 'Petrov'
        , 'Email': 'Petrov_Ivan@example.com'
            }

    # создаю цикл для заполнения обязательных полей
    for i, j in enumerate(dict):
        # формируем css-селектор для поиска элемента на веб-странице
        selector = "input[placeholder*='" + list(dict.keys())[i].lower() + "'"
        # заполняем поле ввода по css-селектору
        browser.find_element(By.CSS_SELECTOR, selector).send_keys(dict.get(j))

    file_path = path.abspath('') + '/empty.txt'
    browser.find_element(By.CSS_SELECTOR, 'input#file').send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    browser.execute_script('return arguments[0].scrollIntoView(true)', button)
    button.click()


finally:
    sleep(5)
    browser.quit()