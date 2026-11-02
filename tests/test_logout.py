from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import ENTER_BUTTON, LOGIN_EMAIL_FIELD, LOGIN_PASSWORD_FIELD, LOGIN_BUTTON, LOGOUT_BUTTON, AVATAR, USERNAME
from urls import page_url
from data import test_user_pass, test_user_email
class TestLogout:

    def test_logout(self, driver):
        driver.get(page_url)
        driver.find_element(*ENTER_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((LOGIN_EMAIL_FIELD)))
        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(test_user_email)
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(test_user_pass)
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((AVATAR)))
        driver.find_element(*LOGOUT_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.invisibility_of_element_located((AVATAR)))
        element_enter_button = driver.find_element(*ENTER_BUTTON)
        assert WebDriverWait(driver, 20).until(expected_conditions.invisibility_of_element((AVATAR)))
        assert WebDriverWait(driver, 20).until(expected_conditions.invisibility_of_element((USERNAME)))
        assert element_enter_button.is_displayed()
