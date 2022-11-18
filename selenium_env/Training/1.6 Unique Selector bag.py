import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # elements = browser.find_elements(By.CSS_SELECTOR, 'input:required')
    # for element in elements:
    #    element.send_keys("Мой ответ")
    input1 = browser.find_element(By.CSS_SELECTOR, "input.first:required")
    input1.send_keys("Bla")
    input2 = browser.find_element(By.CSS_SELECTOR, "input.second:required")
    input2.send_keys("BlaBla")
    input3 = browser.find_element(By.CSS_SELECTOR, "input.third:required")
    input3.send_keys("Bla@bla.com")
    time.sleep(5)

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
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()