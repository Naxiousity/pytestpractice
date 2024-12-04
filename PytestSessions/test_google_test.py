from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

driver = None

def setup_module(module):
    global driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

def teardown_module(module):
    driver.quit

def test_google_title():
    
    assert driver.title == "Google"
    
def test_google_url():
    assert driver.current_url == "https://www.google.com/"