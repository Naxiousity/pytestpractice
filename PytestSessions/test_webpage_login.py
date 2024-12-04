from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def test_google():
    # Initialize Chrome WebDriver using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get("https://www.google.com")
    
    # Perform any additional actions here
    
    driver.quit()  # Don't forget to close the browser after the test

def test_facebook():
    # Initialize Chrome WebDriver using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get("https://www.facebook.com")
    
    # Perform any additional actions here
    
    driver.quit()  # Don't forget to close the browser after the test

def test_reddit():
    # Initialize Chrome WebDriver using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get("https://www.reddit.com")
    
    # Perform any additional actions here
    
    driver.quit()  # Don't forget to close the browser after the test

