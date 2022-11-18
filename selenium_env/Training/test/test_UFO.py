import pytest
import  time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email="123@gmail.com"
psw = "password"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url',
                         ["https://stepik.org/lesson/236895/step/1"
                          , "https://stepik.org/lesson/236896/step/1"
                          , "https://stepik.org/lesson/236897/step/1"
                          , "https://stepik.org/lesson/236898/step/1"
                          , "https://stepik.org/lesson/236899/step/1"
                          , "https://stepik.org/lesson/236903/step/1"
                          , "https://stepik.org/lesson/236904/step/1"
                          , "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, url):
    link = f"{url}"
    browser.get(link)
    login = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "ember32"))
    )
    login.click()
    browser.switch_to.active_element
    input_name = browser.find_element(By.CSS_SELECTOR, '#id_login_email')
    input_name.send_keys(email)
    input_psw = browser.find_element(By.CSS_SELECTOR, '#id_login_password')
    input_psw.send_keys(psw)
    log_in = browser.find_element(By.CLASS_NAME, 'sign-form__btn')
    log_in.click()
    time.sleep(2)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
    text_area = browser.find_element(By.TAG_NAME, "textarea")
    answer = math.log(int(time.time()))
    text_area.send_keys(answer)
    print(answer)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    submit = browser.find_element(By.CLASS_NAME,'submit-submission')
    submit.click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".smart-hints__hint")))
    respond = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    print(respond.text)

    time.sleep(1)


