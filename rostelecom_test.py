from selenium import webdriver
from selenium.webdriver.common.by import By
from config import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import time


@pytest.fixture(autouse=True)
def testing():
    selenium = webdriver.Chrome()
    selenium.implicitly_wait(6)
    selenium.get('https://b2c.passport.rt.ru')
    yield selenium
    selenium.quit()


""" Пользователь переходит на страницу регистрации """
def test_opening_registration_page(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    selenium.find_element(By.ID, 'kc-register').click()
    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Регистрация', print('Тест провален')
    assert selenium.find_element(By.TAG_NAME, 'p').text == 'Личные данные', print('Тест провален')
    assert selenium.find_element(By.XPATH, '//button[@type="submit"]'), print('Тест провален')


""" Пользователь может открыть чат поддержки, перейдя на страницу регистрации """
def test_opening_chat_registration_page(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    selenium.find_element(By.ID, 'kc-register').click()
    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'widget_bar')))
    selenium.find_element(By.ID, 'widget_bar').click()
    time.sleep(3)
    assert selenium.find_element(By.ID, 'widget_sendPrechat')


""" Регистрация на сайте с валидными данными """
def test_registration(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(selenium, 6).until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    selenium.find_element(By.ID, 'kc-register').click()
    selenium.find_element(By.NAME, 'firstName').send_keys(valid_name)
    selenium.find_element(By.NAME, 'lastName').send_keys(valid_surname)
    selenium.find_element(By.ID, 'address').send_keys(valid_email)
    selenium.find_element(By.ID, 'password').send_keys(valid_password)
    selenium.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)
    selenium.find_element(By.ID, 'rt-code-0').send_keys(valid_code)
    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Подтверждение email'


""" Регистрация пользователя с неверным вводом всех полей  """
def test_registration_2(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    selenium.find_element(By.ID, 'kc-register').click()
    selenium.find_element(By.NAME, 'firstName').send_keys(invalid_name)
    selenium.find_element(By.NAME, 'lastName').send_keys(invalid_surname)
    selenium.find_element(By.ID, 'address').send_keys(invalid_email)
    selenium.find_element(By.ID, 'password').send_keys(invalid_password)
    selenium.find_element(By.ID, 'password-confirm').send_keys(invalid_password)
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)


""" Регистрация пользователя с вводом неверного кода доступа """
def test_registration_4(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    selenium.find_element(By.ID, 'kc-register').click()
    selenium.find_element(By.NAME, 'firstName').send_keys(valid_name)
    selenium.find_element(By.NAME, 'lastName').send_keys(valid_surname)
    selenium.find_element(By.ID, 'address').send_keys(valid_email)
    selenium.find_element(By.ID, 'password').send_keys(valid_password)
    selenium.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)
    selenium.find_element(By.ID, 'rt-code-0').send_keys(invalid_code)
    time.sleep(3)


""" Регистрация пользователя с невалидным вводом всех полей - символы """
def test_registration_5(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    selenium.find_element(By.ID, 'kc-register').click()
    selenium.find_element(By.NAME, 'firstName').send_keys(invalid_name_2)
    selenium.find_element(By.NAME, 'lastName').send_keys(invalid_surname_2)
    selenium.find_element(By.ID, 'address').send_keys(invalid_email_2)
    selenium.find_element(By.ID, 'password').send_keys(invalid_password_2)
    selenium.find_element(By.ID, 'password-confirm').send_keys(invalid_password_2)
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)   # задержка 3 секунды


""" Регистрация пользователя с невалидным вводом всех полей (русская и английская раскладка) """
def test_registration_6(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    selenium.find_element(By.ID, 'kc-register').click()
    selenium.find_element(By.NAME, 'firstName').send_keys(invalid_name_3)
    selenium.find_element(By.NAME, 'lastName').send_keys(invalid_surname_3)
    selenium.find_element(By.ID, 'address').send_keys(invalid_email_3)
    selenium.find_element(By.ID, 'password').send_keys(invalid_password_3)
    selenium.find_element(By.ID, 'password-confirm').send_keys(invalid_password_3)
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)



""" Пользователь ввёл в поле "Подтверждение пароля" пароль, отличный от пароля "Новый пароль" то под полем "Подтверждение" отображается "Пароли не совпадают" """
def test_registration_7(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    selenium.find_element(By.ID, 'kc-register').click()
    selenium.find_element(By.NAME, 'firstName').send_keys(valid_name)
    selenium.find_element(By.NAME, 'lastName').send_keys(valid_surname)
    selenium.find_element(By.ID, 'address').send_keys(valid_email)
    selenium.find_element(By.ID, 'password').send_keys(valid_password)
    selenium.find_element(By.ID, 'password-confirm').send_keys(invalid_password_4)
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)



""" Регистрация пользователя, который уже зарегистрирован """
def test_registration_8(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    selenium.find_element(By.ID, 'kc-register').click()
    selenium.find_element(By.NAME, 'firstName').send_keys(valid_name)
    selenium.find_element(By.NAME, 'lastName').send_keys(valid_surname)
    selenium.find_element(By.ID, 'address').send_keys(valid_email)
    selenium.find_element(By.ID, 'password').send_keys(valid_password)
    selenium.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)
    assert selenium.find_element(By.TAG_NAME, 'h2').text == 'Учётная запись уже существует', print('Ошибка')



""" Пользователь может открыть чат поддержки на странице авторизации """
def test_opening_chat_authorization_page(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))
    selenium.find_element(By.ID, 'widget_bar').click()
    time.sleep(3)
    assert selenium.find_element(By.ID, 'widget_sendPrechat'), print('ошибка')


""" Выбора авторизации по полю "Номер" """
def test_opening_authorization_page_2(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    time.sleep(3)
    assert selenium.find_element(By.ID, 't-btn-tab-phone').text == 'Номер'



""" Выбор авторизации по лицевому счету и паролю, "Лицевой счёт" """
def test_opening_authorization_page_5(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))
    selenium.find_element(By.ID, 't-btn-tab-ls').click()
    time.sleep(3)
    assert selenium.find_element(By.ID, 't-btn-tab-ls').text == 'Лицевой счёт'


""" Авторизация с помощью валидных введённых данных (мобильный телефон и пароль)"""
def test_authorization(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    selenium.find_element(By.ID, 'username').send_keys(valid_phone)
    selenium.find_element(By.ID, 'password').send_keys(valid_password)
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)
    assert selenium.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные'


""" Авторизация с помощью валидных введённых данных (электронная почта и пароль) (действующий аккаунт)"""
def test_authorization_2(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 'kc-login')))
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    selenium.find_element(By.ID, 'username').send_keys(valid_email)
    selenium.find_element(By.ID, 'password').send_keys(valid_password)
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)
    assert selenium.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные'


""" Пользователь может перейти на страницу "Восстановление пароля" """
def test_password_recovery(testing):
    selenium = testing
    selenium.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(selenium, 7).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-login')))
    selenium.find_element(By.ID, 'forgot_password').click()
    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Восстановление пароля', print('Тест провален')
    assert selenium.find_element(By.TAG_NAME, 'p').text == 'Введите данные и нажмите «Продолжить»', print('Тест провален')