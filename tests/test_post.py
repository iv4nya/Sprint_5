import random
import string
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MAKE_POST_BUTTON, FUTER, NEXT_PAGE_BUTTON, APPLY_BUTTON, MODAL_HEADING_UNAUTHORIZED_USER_MAKE_POST, SAVE_CHANGES_BUTTON, ENTER_BUTTON, AVATAR, LOGIN_EMAIL_FIELD, LOGIN_PASSWORD_FIELD, LOGIN_BUTTON, ADD_PHOTO_BUTTON_1, PRODUCT_NAME, CATEGORY_DROPDOWN_BUTTON, CATEGORY_DROPDOWN_BOOK, RADIOBUTTON_BU, CITY_DROPDOWN_BUTTON, CITY_DROPDOWN_NOVOSIBIRSK, PRODUCT_DESCRIPTION, PRODUCT_COST, PRODUCT_POST_BUTTON, my_post_header

class TestMakePost():

    def test_make_post_unauthorized_user(self, driver, page_url):
        driver.get(page_url)
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((ENTER_BUTTON)))
        driver.find_element(*MAKE_POST_BUTTON).click()
        assert WebDriverWait(driver, 20).until(expected_conditions. visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[1]/h1')))
        element_modal_heading = driver.find_element(*MODAL_HEADING_UNAUTHORIZED_USER_MAKE_POST)
        assert element_modal_heading.text == 'Чтобы разместить объявление, авторизуйтесь'
        driver.quit()

    def test_make_post_authorized_user(self, driver, page_url, test_user_email, test_user_pass):
        driver.get(page_url)
        driver.find_element(*ENTER_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[1]/h1')))
        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(test_user_email)
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(test_user_pass)
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((AVATAR)))
        driver.find_element(*MAKE_POST_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions. visibility_of_element_located((ADD_PHOTO_BUTTON_1)))
        letters = ''.join(random.choices(string.ascii_letters, k=4))
        digits = ''.join(random.choices(string.digits, k=4))
        product_name = letters + digits
        driver.find_element(*PRODUCT_NAME).send_keys(product_name)
        driver.find_element(*CATEGORY_DROPDOWN_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((CATEGORY_DROPDOWN_BOOK)))
        driver.find_element(*CATEGORY_DROPDOWN_BOOK).click()
        driver.find_element(*RADIOBUTTON_BU).click()
        driver.find_element(*CITY_DROPDOWN_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((CITY_DROPDOWN_NOVOSIBIRSK)))
        driver.find_element(*CITY_DROPDOWN_NOVOSIBIRSK).click()
        driver.find_element(*PRODUCT_DESCRIPTION).send_keys('123')
        element_post_button = driver.find_element(*PRODUCT_POST_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", element_post_button)
        driver.find_element(*PRODUCT_COST).send_keys('101')
        driver.find_element(*PRODUCT_POST_BUTTON).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((APPLY_BUTTON)))
        driver.find_element(*AVATAR).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((SAVE_CHANGES_BUTTON)))
        element_futer = driver.find_element(*FUTER)
        driver.execute_script("arguments[0].scrollIntoView();", element_futer)
        time.sleep(2)       
        while not driver.find_elements(*my_post_header(product_name)):
            driver.find_element(*NEXT_PAGE_BUTTON).click()
        element_new_card = driver.find_element(*my_post_header(product_name))
        assert element_new_card.is_displayed()
        assert element_new_card.text == product_name
        driver.quit()