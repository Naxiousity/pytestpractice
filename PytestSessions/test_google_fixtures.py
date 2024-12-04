from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("--------==============SETUP==========-----------")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

    yield
    print("--------==============ENDOU==========-----------")
    driver.quit

@pytest.mark.usefixtures("init_driver")
def test_google_title(init_driver):
    
    assert driver.title == "Googlel"

@pytest.mark.usefixtures("init_driver")    
def test_google_url(init_driver):
    assert driver.current_url == "https://www.google.com/"