import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, '[type="text"]')
    for element in elements:
        element.send_keys("Мой ответ")
    # Ваш код, который заполняет обязательные поля
    # input1 = browser.find_element(By.NAME, "firstname")
    # input1.send_keys("Bla")
    # input2 = browser.find_element(By.NAME, "lastname")
    # input2.send_keys("BlaBla")
    # input3 = browser.find_element(By.NAME, "email")
    # input3.send_keys("Bla@bla.com")

    # current_dir = os.path.abspath(os.path.dirname('file.txt'))  # получаем путь к директории текущего исполняемого файла
    # file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    # print(current_dir)
    print(os.path.abspath('file.txt'))
    f = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    f.send_keys(os.path.abspath('file.txt'))
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()