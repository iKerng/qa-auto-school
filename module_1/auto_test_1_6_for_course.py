from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# объявляем ссылку, форму которой будем тестировать
link = "http://suninjuly.github.io/registration2.html"

# создаю словарь со списком полей и их значением для заполнения
dict = {
    'First name': 'Ivan'
    , 'Last name': 'Petrov'
    , 'Email': 'Petrov_Ivan@example.com'
}

try:
    # открываем ссылку в вебдрайвере
    browser = webdriver.Chrome()
    browser.get(link)

    # создаю цикл для заполнения обязательных полей
    for i, j in enumerate(dict):
        # формируем css-селектор для поиска элемента на веб-странице
        selector = "input[placeholder*='" + list(dict.keys())[i].lower() + "'"
        # заполняем поле ввода по css-селектору
        browser.find_element(By.CSS_SELECTOR, selector).send_keys(dict.get(j))


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()