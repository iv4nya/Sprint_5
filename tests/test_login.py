from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import ENTER_BUTTON, LOGIN_BUTTON, LOGIN_EMAIL_FIELD, LOGIN_PASSWORD_FIELD, AVATAR, USERNAME

class TestLogin:

    def test_login(self, driver, page_url, test_user_email, test_user_pass):
        driver.get(page_url)
        driver.find_element(*ENTER_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[1]' )))
        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(test_user_email)
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(test_user_pass)
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((AVATAR)))
        target_url = 'https://qa-desk.education-services.ru/login'
        assert driver.current_url == target_url
        element_avatar = driver.find_element(*AVATAR)
        element_username = driver.find_element(*USERNAME)
        assert element_avatar.is_displayed()
        assert element_username.is_displayed()
        driver.quit()