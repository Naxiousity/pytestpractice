import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from datetime import datetime

@pytest.fixture(scope='class')
def init_driver(request):
    print("--------==============SETUP==========-----------")
    
    # service = Service(ChromeDriverManager().install())
    print(datetime.now())
    ch_driver = webdriver.Chrome()
    print(datetime.now())
    request.cls.driver = ch_driver

    yield
    ch_driver.close()