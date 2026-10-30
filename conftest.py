import pytest
from selenium import webdriver
import random
import string

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver

@pytest.fixture
def rndemail():
    chars = string.ascii_lowercase + string.digits
    username = "".join(random.choice(chars) for _ in range(7))
    domain = "".join(random.choice(chars) for _ in range(4))
    return f'{username}@{domain}.ru'

@pytest.fixture
def rndemail_not_mask():
    chars = string.ascii_lowercase + string.digits
    username = "".join(random.choice(chars) for _ in range(10))
    domain = "".join(random.choice(chars) for _ in range(2))
    return f'{username}@{domain}ru'

@pytest.fixture
def test_user_email():
    return '123123@123.ru'

@pytest.fixture
def test_user_pass():
    return '123'

@pytest.fixture
def page_url():
    return 'https://qa-desk.education-services.ru/'