from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import ENTER_BUTTON, NO_ACCAUNT_BUTTON, REG_EMAIL_FIELD, REG_PASSWORD_FIELD, REG_PASSWORD_REPEAT_FIELD, CREATE_ACCAUNT_BUTTON, REG_EMAIL_ERROR_FIELD, REG_PASSWORD_ERROR_FIELD, REG_PASSWORD_ERROR_REPEAT_FIELD, AVATAR, REG_ERROR_TEXT
from urls import page_url
from data import test_user_email, test_user_pass
from helpers import rndemail, rndemail_not_mask

class TestRegistration:

    def test_user_registration(self, driver):
        driver.get(page_url)
        driver.find_element(*ENTER_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((NO_ACCAUNT_BUTTON)))
        driver.find_element(*NO_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((REG_EMAIL_FIELD)))
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((REG_PASSWORD_FIELD)))
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((REG_PASSWORD_REPEAT_FIELD)))
        driver.find_element(*REG_EMAIL_FIELD).send_keys(rndemail())
        driver.find_element(*REG_PASSWORD_FIELD).send_keys('123')
        driver.find_element(*REG_PASSWORD_REPEAT_FIELD).send_keys('123')
        driver.find_element(*CREATE_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((AVATAR)))
        targer_url = 'https://qa-desk.education-services.ru/regiatration'
        assert driver.current_url == targer_url
        element = driver.find_element(*AVATAR)
        assert element.is_displayed()

    def test_user_registration_not_mask(self, driver):
        driver.get(page_url)
        driver.find_element(*ENTER_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((NO_ACCAUNT_BUTTON)))
        driver.find_element(*NO_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((REG_EMAIL_FIELD)))
        driver.find_element(*REG_EMAIL_FIELD).send_keys(rndemail_not_mask())
        driver.find_element(*REG_PASSWORD_FIELD).send_keys('123')
        driver.find_element(*REG_PASSWORD_REPEAT_FIELD).send_keys('123')
        driver.find_element(*CREATE_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((REG_ERROR_TEXT)))
        element_error_text = driver.find_element(*REG_ERROR_TEXT)
        assert 'Ошибка' in element_error_text.text
        fields = [REG_EMAIL_ERROR_FIELD, REG_PASSWORD_ERROR_FIELD, REG_PASSWORD_ERROR_REPEAT_FIELD]
        for locator in fields:
            field = driver.find_element(*locator)
            border = field.value_of_css_property('border')

            assert border == '0.666667px solid rgb(255, 105, 114)'

    def test_user_registration_previously_created(self, driver):
        driver.get(page_url)
        driver.find_element(*ENTER_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((NO_ACCAUNT_BUTTON)))
        driver.find_element(*NO_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((REG_EMAIL_FIELD)))
        driver.find_element(*REG_EMAIL_FIELD).send_keys(test_user_email)
        driver.find_element(*REG_PASSWORD_FIELD).send_keys(test_user_pass)
        driver.find_element(*REG_PASSWORD_REPEAT_FIELD).send_keys(test_user_pass)
        driver.find_element(*CREATE_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((REG_ERROR_TEXT)))
        element_error_text = driver.find_element(*REG_ERROR_TEXT)
        assert 'Ошибка' in element_error_text.text
        fields = [REG_EMAIL_ERROR_FIELD, REG_PASSWORD_ERROR_FIELD, REG_PASSWORD_ERROR_REPEAT_FIELD]
        for locator in fields:
            field = driver.find_element(*locator)
            border = field.value_of_css_property('border')
        
            assert border == '0.666667px solid rgb(255, 105, 114)'