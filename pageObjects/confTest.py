import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    options.add_experimental_option("detach", True)
    return driver

def setup():
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    options.add_experimental_option("detach", True)
    return driver

def setup():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    return driver




