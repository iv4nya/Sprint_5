from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import ENTER_BUTTON, NO_ACCAUNT_BUTTON, REG_EMAIL_FIELD, REG_PASSWORD_FIELD, REG_PASSWORD_REPEAT_FIELD, CREATE_ACCAUNT_BUTTON, REG_EMAIL_ERROR_FIELD, REG_PASSWORD_ERROR_FIELD, REG_PASSWORD_ERROR_REPEAT_FIELD

class TestRegistration:

    def test_user_registration(self, driver, rndemail, page_url):
        driver.get(page_url)
        driver.find_element(*ENTER_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[2]' )))
        driver.find_element(*NO_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[1]/h1' )))
        driver.find_element(*REG_EMAIL_FIELD).send_keys(rndemail)
        driver.find_element(*REG_PASSWORD_FIELD).send_keys('123')
        driver.find_element(*REG_PASSWORD_REPEAT_FIELD).send_keys('123')
        driver.find_element(*CREATE_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'circleSmall' )))
        targer_url = 'https://qa-desk.education-services.ru/regiatration'
        assert driver.current_url == targer_url
        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/button' )
        assert element.is_displayed()
        driver.quit

    def test_user_registration_not_mask(self, driver, rndemail_not_mask, page_url):
        driver.get(page_url)
        driver.find_element(*ENTER_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[2]' )))
        driver.find_element(*NO_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[1]/h1' )))
        driver.find_element(*REG_EMAIL_FIELD).send_keys(rndemail_not_mask)
        driver.find_element(*REG_PASSWORD_FIELD).send_keys('123')
        driver.find_element(*REG_PASSWORD_REPEAT_FIELD).send_keys('123')
        driver.find_element(*CREATE_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/span')))
        element_error_text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/span')
        assert 'Ошибка' in element_error_text.text
        fields = [REG_EMAIL_ERROR_FIELD, REG_PASSWORD_ERROR_FIELD, REG_PASSWORD_ERROR_REPEAT_FIELD]
        for locator in fields:
            field = driver.find_element(*locator)
            border = field.value_of_css_property('border')

            assert border == '0.666667px solid rgb(255, 105, 114)'
        driver.quit

    def test_user_registration_previously_created(self, driver, test_user_email, test_user_pass, page_url):
        driver.get(page_url)
        driver.find_element(*ENTER_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[2]' )))
        driver.find_element(*NO_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[1]/h1' )))
        driver.find_element(*REG_EMAIL_FIELD).send_keys(test_user_email)
        driver.find_element(*REG_PASSWORD_FIELD).send_keys(test_user_pass)
        driver.find_element(*REG_PASSWORD_REPEAT_FIELD).send_keys(test_user_pass)
        driver.find_element(*CREATE_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'input_span__yWPqB')))
        element_error_text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/span')
        assert 'Ошибка' in element_error_text.text
        fields = [REG_EMAIL_ERROR_FIELD, REG_PASSWORD_ERROR_FIELD, REG_PASSWORD_ERROR_REPEAT_FIELD]
        for locator in fields:
            field = driver.find_element(*locator)
            border = field.value_of_css_property('border')
        
            assert border == '0.666667px solid rgb(255, 105, 114)'
        driver.quit